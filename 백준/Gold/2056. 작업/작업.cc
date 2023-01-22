#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N,K,P,total;

vector<vector<int>> graph;
vector<int> indegree;
queue<int> q;
vector<int> cost;
int dp[10001]={0};

void topology_sort()
{
    total=0;

    for (int i = 1; i <= N ; i++)
    {
        if (indegree[i]==0)
        {
            q.push(i);
            dp[i]=cost[i];
        }
    }

    for (int i = 1 ; i <=N ; i++)
    {
        int node = q.front();
        total=max(total , dp[node]);
        q.pop();

        for (int j=0 ; j < graph[node].size() ; j++)
        {
            int next_node = graph[node][j];
            dp[next_node] = max(dp[node]+cost[next_node] , dp[next_node]); 

            if (--indegree[next_node]==0)
            {
                q.push(next_node);
            }
        }
    }
    cout << total;

}

void input()
{
    cin >> N;

    graph.assign(N+1, vector<int> (0,0) );
    indegree.assign(N+1,0);
    cost.assign(N+1,0);

    for (int i = 1 ; i <= N ; i++)
    {
        cin >> cost[i];
        cin >> K;

        for (int j=0 ; j<K ; j++)
        {
            cin >> P;
            graph[i].push_back(P);
            indegree[P]++;
        }
    }
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    input();
    topology_sort();

}