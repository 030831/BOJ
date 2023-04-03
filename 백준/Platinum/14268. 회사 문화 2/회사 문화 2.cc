#include <bits/stdc++.h>
#define MAX 100001
using namespace std;

/**
 * 백준 14268 - 회사문화 2
 *
 * 1 i w: i번째 직원이 직속 상사로부터 w만큼 칭찬을 받는다. (2 ≤ i ≤ n, 1 ≤ w ≤ 1,000)
 * 2 i: i번째 직원이 칭찬을 받은 정도를 출력한다.
 */

int N,M,K;
int cnt , ans;
int START[MAX] , END[MAX];
vector<int> tree(4*MAX);
vector<int> lazy(4*MAX);
vector<vector<int>> graph(4*MAX);
bool visited[MAX];

void lazy_update(int node,  int start , int end)
{
    if (lazy[node])
    {
        tree[node] += (end-start+1)*lazy[node];
        if (start!=end)
        {
            lazy[node*2]+=lazy[node];
            lazy[node*2+1]+=lazy[node];
        }
        lazy[node] = 0;
    }
}

void update(int node , int start , int end , int left , int right , int value)
{
    lazy_update(node , start , end);

    if (left>end || right<start)
    {
        return;
    }

    if (left<=start && right>=end)
    {
        tree[node] += (end-start+1)*value;

        if (start!=end)
        {
            lazy[node*2]+=value;
            lazy[node*2+1]+=value;
        }
        return;
    }

    update(node*2 , start , (start+end)/2 , left , right , value);
    update(node*2+1 , (start+end)/2+1 , end , left, right , value);
    tree[node] = tree[node*2] + tree[node*2+1];
}

void query(int node , int start, int end , int index)
{
    lazy_update(node , start , end);
    if (index<start || index>end)
    {
        return;
    }
    if (start==end)
    {
        ans = tree[node];
        return;
    }

    query(node*2 , start , (start+end)/2 , index);
    query(node*2+1 , (start+end)/2+1 , end , index);
}

void dfs(int node)
{
    visited[node] = true;
    START[node]=++cnt;

    for (int nextNode : graph[node])
    {
        if (!visited[nextNode])
        {
            dfs(nextNode);
        }
    }

    END[node] = cnt;
}


void input()
{
    cin >> N >> M;

    for (int i = 0 ; i < N ; i++)
    {
        cin >> K;
        if (K != -1) {
            graph[K].push_back(i+1);
        }
    }

    dfs(1);


    for (int i = 0 ; i < M ; i++)
    {
        int a,b,c;
        cin >> a;

        if (a==1)
        {
            cin >> b >> c;
            update(1,1,N,START[b] , END[b] , c);
        }
        else
        {
            cin >> b;
            query(1,1,N,START[b]);
            cout << ans << '\n';
        }
    }

}
int main()
{
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    input();
}