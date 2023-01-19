/*
선택한 노드끼리는 서로 인접해서는 안된다.
dp[cur][0] - 노드를 선택하지 않음.
dp[cur][1] - 노드를 선택함.

dp[cur][0] = dp[cur][0] + max(dp[next][0]+dp[next][1]) 
선택하지 않았을 경우 자식노드은 선택하지 않거나 선택하거나 둘중하나.

dp[cur][1] = dp[cur][1] + dp [next][0]

선택할 경우 자식노드는 선택하지 않아야함.

문제는 이때의 최대값을 구할 수 있으나 경로를 구해야 함.
dp[cur][0] 에서 자식노드를 선택할 경우를 저장하고 - 조건 (값에 따라 조건선택)
dp[cur][1] 에서 현재 노드를 저장한다.  - 필수 (무조건 선택하기 때문)

자신이 선택되었을 때의 최댓값이 선택되지 않았을때의 최댓값보다 크다면 해당 노드는 최댓값을 이루는 구성요소가 된다.
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int dp[10001][2]={0,};
int Node[10001]={0};
vector<int> path;

int DFS(int node , vector<vector<int>> &graph , vector<bool> &visit , vector<int> &cost)
{
    visit[node]=true;
    dp[node][1]=cost[node];

    
    for (auto next_node : graph[node])
    {
        if (!visit[next_node])
        {
            DFS(next_node , graph , visit , cost);
            dp[node][0]=dp[node][0]+max(dp[next_node][0] , dp[next_node][1] );
            dp[node][1]=dp[node][1]+dp[next_node][0];
            
        }
    }
    return max(dp[1][0] , dp[1][1]);
}

void Tracking(int node , int pre , vector<vector<int>> &graph ,  vector<bool> &visit)
{
    // 만약 자신이 선택되었을때 최대값이 되었다면 , 그리고 이전노드는 방문하지 않았다면
    if (dp[node][1]>dp[node][0] && !visit[pre]) 
    {
        path.push_back(node);
        visit[node]=true; 
    }

    for (auto next_node : graph[node])
    {
        if (next_node==pre) // 이전노드랑 같다면 넘긴다.
        {
            continue;
        }
        if (!visit[next_node])
        {
            Tracking(next_node , node , graph , visit);
        }
    }
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;

    cin >> N;

    vector<int> cost (N+1,0);

    for (int i = 1 ; i <= N ; i++)
    {
        cin >> cost[i];
    }

    vector<vector<int>> graph(N+1);
    vector<bool> visit(N+1);

    for (int i = 0 ; i < N-1 ; i ++)
    {
        int a,b;

        cin >> a >> b;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    cout << DFS(1,graph,visit,cost) << "\n";
    

    fill(visit.begin() , visit.end() , false);

    Tracking(1, 0 ,graph ,visit);

    sort(path.begin() , path.end());

    for (auto x:path)
    {
        cout << x << " ";
    }

}
