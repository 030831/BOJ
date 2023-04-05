#include <bits/stdc++.h>

#define MAX 100001

using namespace std;

int N,M,K,cnt;

vector<vector<int>> graph(MAX);
vector<int> treeDown(4*MAX);
vector<int> treeUp(4*MAX);
vector<int> lazyDown(4*MAX);
vector<int> lazyUp(4*MAX);

int START[MAX] , END[MAX];

/**
 * 백준 14228 - 회사문화 3
 *
 */


void dfs(int node)
{
    START[node] = ++cnt;

    for (int nextNode : graph[node])
    {
        dfs(nextNode);
    }

    END[node] = cnt;
}

void lazyDown_update(int node , int start , int end)
{
    if (lazyDown[node])
    {
        treeDown[node] += (end-start+1) * lazyDown[node];

        if (start!=end)
        {
            lazyDown[node<<1] += lazyDown[node];
            lazyDown[node<<1|1] += lazyDown[node];
        }
        lazyDown[node] = 0;
    }
}

void lazyUp_update(int node , int start , int end)
{
    if (lazyUp[node])
    {
        treeUp[node] += (end-start+1) * lazyUp[node];

        if (start!=end)
        {
            lazyUp[node<<1] += lazyUp[node];
            lazyUp[node<<1|1] += lazyUp[node];
        }
        lazyUp[node] = 0;
    }
}

void treeUp_update(int node , int start , int end , int left , int right ,int value)
{
    lazyUp_update(node , start , end);

    if (left>end || right<start)
    {
        return;
    }

    if (left<=start && right>=end)
    {
        treeUp[node]+=(end-start+1)*value;

        if (start!=end)
        {
            lazyUp[node<<1]+=value;
            lazyUp[node<<1|1]+=value;
        }
        return;
    }


    int mid = (start+end)/2;
    treeUp_update(node<<1 , start , mid , left , right , value);
    treeUp_update(node<<1|1 , mid+1 , end , left, right , value);
    treeUp[node] = treeUp[node<<1] + treeUp[node<<1|1];
}

int query_treeUp(int node , int start , int end , int index)
{
    lazyUp_update(node , start , end);

    if (index>end || index<start)
    {
        return 0;
    }

    if (start==end)
    {
        return treeUp[node];
    }
    int mid = (start+end)/2;
    return query_treeUp(node<<1 , start , mid , index ) + query_treeUp(node<<1|1 , mid+1 , end , index);
}
void treeDown_update(int node , int start , int end , int left , int right , int value)
{

    lazyDown_update(node , start , end);

    if (left>end || right<start)
    {
        return;
    }

    if (left<=start && right>=end)
    {
        treeDown[node] += (end-start+1) * value;

        if (start!=end)
        {
            lazyDown[node<<1] += value;
            lazyDown[node<<1|1] += value;
        }

        return;
    }

    int mid = (start+end)/2;
    treeDown_update(node<<1 , start , mid , left , right , value);
    treeDown_update(node<<1|1 , mid+1 , end , left, right , value);
    treeDown[node] = treeDown[node<<1] + treeDown[node<<1|1];

}

int query_treeDown(int node , int start , int end , int left , int right)
{

    lazyDown_update(node , start ,end);

    if (left>end || right<start)
    {
        return 0;
    }

    if (left<=start && right>=end)
    {
        return treeDown[node];
    }

    int mid = (start+end)/2;
    return query_treeDown(node<<1 , start , mid , left ,right ) + query_treeDown(node<<1|1 , mid+1 , end , left , right);
}

int main()
{
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    cin >> N >> M;

    for (int i = 1 ; i<=N ; i++)
    {
        cin >> K;
        if (K!=-1)
        {
            graph[K].push_back(i);
        }
    }

    dfs(1);


    int time = 1;
    for (int i = 0 ; i < M ; i++)
    {
        int a,b,c;
        cin >> a;

        if (a==1)
        {
            cin >> b >> c;
            if (time==0)
            {
                treeDown_update(1,1,N, START[b] , START[b] , c);
            }
            else
            {
                treeUp_update(1,1,N , START[b] , END[b], c);
            }
        }
        else if (a==2)
        {
            cin >> b;
            cout << query_treeDown(1,1,N,START[b] ,END[b])+query_treeUp(1,1,N,START[b]) << '\n';
        }
        else
        {
            if (time==0)
            {
                time =1;
            }
            else
            {
                time = 0;
            }
        }



    }
}