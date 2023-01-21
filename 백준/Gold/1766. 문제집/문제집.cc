#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N,M;
int s,e;

vector<vector<int>> graph;
vector<int> indegree;
priority_queue<int , vector<int> , greater<int> > pq;

void query()
{

    for (int i = 1 ; i <=N; i++)
    {
        if (indegree[i]==0)
        {
            pq.push(i);
        }
    }

    for (int i = 1 ; i <=N ; i++)
    {
        int node = pq.top();
        pq.pop();

        cout << node << " ";

        for (int j = 0 ; j < graph[node].size() ; j++)
        {
            //sort(graph[node].begin() , graph[node].end());

            int next_node = graph[node][j];

            if (--indegree[next_node]==0)
            {
                pq.push(next_node);
            }
        }
        
    }
}

void input()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;

    graph.assign(N+1, vector<int> (0,0) );
    indegree.assign(N+1, 0);

    for (int i = 0 ; i < M ; i++)
    {
        cin >> s >> e;

        graph[s].emplace_back(e);
        indegree[e]++;
    }

}

int main()
{
    input();

    query();
}