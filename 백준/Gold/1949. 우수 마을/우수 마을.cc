/*
일반 마을은 자식 마을이 우수거나, 자식 마을이 일반 마을이다.
더 큰 쪽을 선택한다. 문제의 3번 조건은 여기서 해결이 된다.
dp[node][0]=dp[node][0]+max(dp[next_node][0],dp[next_node][1]);

현재 마을이 우수 마을이면, 자식은 반드시 일반 마을이어야 한다.
dp[node][1]=dp[node][1]+dp[next_node][0];
*/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <deque>

using namespace std;
int dp[10000][2];

void DFS(int node , vector<bool> &visit , vector<vector<int>> &L  , vector<int> &cost )
{

    if (visit[node])
    {
        return;
    }
    
    visit[node]=true;
    dp[node][0]=0;
    dp[node][1]=cost[node];


    for (auto next_node :L[node])
    {   

        if (!visit[next_node])
        {
            DFS(next_node , visit , L ,cost);
            dp[node][0]=dp[node][0]+max(dp[next_node][0],dp[next_node][1]);
            dp[node][1]=dp[node][1]+dp[next_node][0];
        }
    }
}
int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;

    cin >> N;

    vector<int> cost(N+1,0);

    for (int i = 1 ; i <=N ; i++)
    {
        cin >> cost[i];
    }

    vector<vector<int>> L(N+1); // 시작노드는 1부터 시작하기 때문에 N+1 로 설정.

    for (int i = 0 ; i < N-1 ; i++)
    {
        int a,b;

        cin >> a >> b;
        L[a].push_back(b);
        L[b].push_back(a);
    }

    vector<bool> visit(N+1,false);

    DFS(1,visit , L, cost);

    cout << max(dp[1][0] , dp[1][1]);
}