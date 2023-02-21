#include <iostream>
#include <queue>
#include <vector>
#include <string.h>

using namespace std;
const int MAX = 903;
const int S = MAX -2 ; // 소스 정점 번호
const int E = MAX -1 ; // 싱크 정점 번호
const int INF = 1000000000;
const int WORK = 400;

vector<int> graph[MAX]; // 그래프
int N,M;
int capacity[MAX][MAX] = {0}; // 각 간선의 용량
int cost[MAX][MAX] = {0}; // 각 간선의 비용
int flow[MAX][MAX] = {0}; // 각 간선에 흐르는 유량

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;

    for (int i = 1 ; i<=N ; ++i) { 
        capacity[S][i] = 1;
        graph[S].push_back(i);
        graph[i].push_back(S);
    }

    for (int i = 1 ; i <= M ; ++i) { 
        graph[i+WORK].push_back(E);
        graph[E].push_back(i+WORK);
        capacity[i+WORK][E] = 1;
    }

    for (int i = 1 ; i <=N ; ++i ) { 
        int cnt ;
        cin >> cnt;
        for (int j = 0 ; j< cnt ; ++j) {
            int Dist , Cost;
            cin >> Dist >> Cost;
            graph[i].push_back(Dist+WORK);
            graph[Dist+WORK].push_back(i);

            cost[i][Dist+WORK] = Cost;
            cost[Dist+WORK][i] = -Cost;
            capacity[i][Dist+WORK ]=1;
        }
    }

    int MIN_Flow = 0;
    int Total = 0;

    while(1) {
        int pre[MAX] , dist[MAX];
        bool visited[MAX] = {0};
        queue<int> Q;

        fill(pre, pre+MAX , -1);
        fill(dist , dist+MAX , INF);

        dist[S] = 0;
        visited[S] = true;

        Q.push(S);
        
        while(!Q.empty()) {
            int node = Q.front();
            Q.pop();

            visited[node] = false;

            for (int next_node : graph[node]) {
                if (capacity[node][next_node] - flow[node][next_node]>0 && dist[next_node] > dist[node] + cost[node][next_node]) {
                    // 유량을 흘릴 수 있고 경로단축이 된다면
                    dist[next_node]=dist[node] + cost[node][next_node] ;
                    pre[next_node] = node;

                    if (!visited[next_node]) {
                        Q.push(next_node);
                        visited[next_node] = true;
                    }
                }
            }
        }

        if (pre[E]==-1) {
            break; // 더이상 경로가없다면
        }
        

        for (int i = E ; i!=S ; i=pre[i]) {
            MIN_Flow+=cost[pre[i]][i];
            flow[pre[i]][i] ++;
            flow[i][pre[i]] --;
        }
        Total ++;
    }
    
    cout << Total << '\n' << MIN_Flow;
}