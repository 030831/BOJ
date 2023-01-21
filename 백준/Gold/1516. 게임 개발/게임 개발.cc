#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N,K;
vector<vector<int>> graph;
vector<int> indegree;
queue<int> q;
vector<int> cost;
int dp[501]={0};

void query()
{

    for (int i = 1 ; i <=N ; i++)
    {
        cout << dp[i]+cost[i] << "\n";
    }

}

void topology_sort()
{


    for (int i = 1 ; i <= N ; i++)
    {
        if (indegree[i]==0)
        {
            q.push(i);
        }
    }

    for (int i = 1;  i<=N ; i++)
    {
        int node = q.front();
        q.pop();

        for (int j = 0 ; j < graph[node].size() ; j++)
        {
            int next_node = graph[node][j];

            dp[next_node]=max(dp[next_node] , dp[node]+cost[node]);

            if (--indegree[next_node]==0)
            {
                q.push(next_node);

            }
        }
    }
}

void input()
{
    cin >> N;

    graph.assign(N+1 , vector<int>(0,0));
    indegree.assign(N+1,0);
    cost.assign(N+1,0);

    for (int i = 1 ; i <=N ; i++)
    {
        cin >> cost[i];

        while (1)
        {
            cin >> K;

            if (K==-1)
            {
                break;
            }
            graph[K].push_back(i);
            indegree[i]++;
        }
    }
}

int main()
{
    input();

    topology_sort();
    
    query();
}