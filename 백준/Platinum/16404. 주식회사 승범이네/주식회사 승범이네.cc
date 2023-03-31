#include <bits/stdc++.h>

#define MAX 100001
using namespace std;

int N,M,K,cnt,ans;
int a,b,c;

vector<vector<int>> graph(4*MAX);
vector<int> tree(4*MAX);
vector<int> lazy(4*MAX);
bool visited[MAX];
int Start[MAX] , End[MAX];
void dfs(int node)
{
    visited[node]=true;
    Start[node]=++cnt;
    for (int i : graph[node])
    {
        if (!visited[i])
        {
            dfs(i);
        }
    }

    End[node]=cnt;
}


void lazy_update(int node , int start , int end)
{
    if (lazy[node])
    {
        tree[node]+=(end-start+1)*lazy[node];
        if (start!=end)
        {
            lazy[node*2]+=lazy[node];
            lazy[node*2+1]+=lazy[node];
        }
        lazy[node]=0;
    }
}

void tree_update(int node , int start , int end , int left , int right , int value)
{
    lazy_update(node , start , end);

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

    tree_update(node*2 , start , (start+end)/2 , left,  right , value);
    tree_update(node*2+1 , (start+end)/2+1 , end , left , right , value);

    tree[node] = tree[node*2] + tree[node*2+1];
}

void query(int node , int start , int end , int index)
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

void input()
{
    cin >> N >> M;

    for (int i = 0 ; i < N ; i++)
    {
        cin >> K;
        if (K!=-1)
        {
            graph[K].push_back(i+1);
        }
    }

    dfs(1);
}

void solve()
{
    for (int i = 0; i < M ; i++)
    {
        cin >> a;
        if (a==1)
        {
            cin >> b >> c;
            tree_update(1,1,N,Start[b] , End[b] , c);
        }
        else
        {
            cin >> b;
            query(1,1,N,Start[b]);
            cout << ans << '\n';
        }
    }
}
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
    input();
    solve();
    
}