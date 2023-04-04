#include <bits/stdc++.h>

#define MAX 100001

using namespace std;

vector<int> tree(4*MAX);
vector<int> lazy(4*MAX);
int START[MAX] , END[MAX];
vector<vector<int>> graph(MAX);

int N,M,K,cnt;

void dfs(int node)
{
    START[node]= ++cnt;
    for (int nextNode : graph[node])
    {
        dfs(nextNode);
    }
    END[node] = cnt;
}

void lazy_update(int node , int start , int end)
{
    if (lazy[node])
    {
        tree[node]+=lazy[node];

        if (start!=end)
        {
            lazy[node*2] +=lazy[node];
            lazy[node*2+1] +=lazy[node];
        }
        lazy[node] = 0;
    }

}

void update(int node , int start , int end , int left , int right , int value)
{
    lazy_update(node,  start , end);

    if (left>end || right<start)
    {
        return;
    }

    if (left<=start && right>=end)
    {
        tree[node]+=(end-start+1)*value;

        if (start!=end)
        {
            lazy[node*2]+=value;
            lazy[node*2+1]+=value;
        }
        return;
    }

    update( node*2, start ,  (start+end)/2, left , right , value);
    update(  node*2+1 , (start+end)/2+1 ,end , left, right , value);

    tree[node] = tree[node*2]+tree[node*2+1];

}

int query(int node , int start, int end , int left , int right)
{
    lazy_update(node , start , end);

    if (left>end || right<start)
    {
        return 0;
    }

    if (left<=start && right>=end)
    {
        return tree[node];
    }

    return query(node*2 , start , (start+end)/2 , left , right) + query(node*2+1 , (start+end)/2+1 , end , left ,right);


}
int main()
{
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    cin >> N >> M;

    for (int i = 1; i <= N ; i++)
    {
        cin >> K;
        if (K!=-1)
        {
            graph[K].push_back(i);
        }

    }

    dfs(1);

    for (int i = 0 ; i < M ; i++)
    {
        int a;
        int b;
        int c;

        cin >> a;

        if (a==1)
        {
            cin >> b >> c;
            update(1,1,N,START[b] , START[b], c);

        }
        else
        {
            cin >> b;

            cout << query(1,1,N , START[b] , END[b]) << '\n';
        }
    }
}

