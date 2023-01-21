#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int T,N,K,W;
int s,e;


long long solve(vector<int> &L , vector<vector<int>> &graph , vector<int> &indegree)
{

    
    queue<int> q; // 큐 비우기

    long long dp[100001]={0};

    for (int i = 1 ; i<=N ; i++)
    {
        if (indegree[i]==0)
        {
            q.push(i);
        }
    }

    for (int i = 1 ; i <=N ; i ++)
    {
        int node=q.front();
    
        q.pop();

        
        for (int j = 0 ; j < graph[node].size() ; j++)
        {
            int next_node= graph[node][j]; 
            
            if (--indegree[next_node]==0)
            {
                q.push(next_node);
            }
            dp[next_node]=max(dp[next_node] , dp[node]+L[node]);
        }
    }
    return dp[W]+L[W];
}
void input()
{
    cin >> T;

    while (T--)
    {
        cin >> N >> K;

        vector<int> L(N+1,0);
        vector<vector<int>> graph(N+1);
        vector<int> indegree(N+1,0);

        for (int i = 1; i <= N;  i++)
        {
            cin >> L[i];
        }

        for (int i = 0 ; i < K ; i++)
        {
            cin >> s >> e;
            graph[s].emplace_back(e);
            indegree[e]++;
        }


        cin >> W;
        

        cout << solve(L, graph , indegree) << "\n";
        
    }

}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    input();

}