#include <iostream>
#include <vector>

using namespace std;

int dp[100001]={0};

void DFS(int node , vector<vector<int>> &graph , vector<bool> &visit)
{
    visit[node]=true;

    for (auto next_node : graph[node])
    {
        if (!visit[next_node])
        {
            dp[next_node]+=dp[node];
            DFS(next_node , graph , visit);

        }
    }
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N,M;
    cin >> N >> M;
    
    vector<vector<int>> graph(N+1);
    vector<bool> visit(N+1);

    for (int i =1 ; i<=N ; i++)
    {
        int K;
        cin >> K;

        if (K!=-1)
        {
            graph[K].push_back(i);
        }
    }



    for (int i = 0 ; i < M ; i++)
    {
        int a,b;
        cin >> a >> b;
        dp[a]+=b;
    }

    DFS(1 , graph ,visit);

    for (int i = 1 ; i <=N ; i++)
    {
        cout << dp[i] << " ";
    }
}

/*

6 6
-1 1 2 3 3 2
2 123
3 123
4 123
5 123
2 123
3 123

0 246 492 615 615 246
*/