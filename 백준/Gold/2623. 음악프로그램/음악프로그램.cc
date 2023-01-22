#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N,M,K;

vector<vector<int>> graph;
vector<int> indegree;
vector<int> answer;
queue<int> q;

void query()
{
    if (answer.size()==N)
    {
        for (auto node : answer)
        {
            cout << node << "\n";
        }
    }
    else
    {
        cout << "0" ;
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

    for (int i = 0 ; i < N ; i++)
    {
        if (q.empty())
        {
            break;
        }
        int node = q.front();
        answer.push_back(node);
        q.pop();

        for (int j = 0 ; j < graph[node].size() ; j++)
        {
            int next_node = graph[node][j];

            if (--indegree[next_node]==0)
            {
                q.push(next_node);
            }
        }
    }
}

void input()
{
    cin >> N >> M;
        
    graph.assign(N+1 ,vector<int> (0,0));
    indegree.assign(N+1,0);

    
    while (M--)
    {
        cin >> K;

        vector<int> check(K,0);

        for (int i = 0 ; i < K ; i++)
        {
            cin >> check[i];
        }

        for (int i = 1 ; i <K ; i++)
        {
            graph[check[i-1]].emplace_back(check[i]);
            indegree[check[i]]++;
        }
    }    
}
int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    input();
    topology_sort();
    query();

}