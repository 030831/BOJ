#include <iostream>
#include <queue>
#include <vector>
#include <string.h>

using namespace std;
const int MAX_N = 100; // 최대 N,M
const int MAX_V = 2*(MAX_N+1); // 최대 정점 개수
const int S = MAX_V -2 ; // 소스 정점 번호
const int E = MAX_V -1 ; // 싱크 정점 번호
const int INF = 1000000000;


int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N,M;
    int capacity[MAX_V][MAX_V] = {0}; // 각 간선의 용량
    int cost[MAX_V][MAX_V] = {0}; // 각 간선의 비용
    int flow[MAX_V][MAX_V] = {0}; // 각 간선에 흐르는 유량

    vector<int> graph[MAX_V]; // 그래프

    cin >> N >> M;

    for (int i = MAX_N ; i<MAX_N+N ; i++) { // 각 사람의 정점과 싱크 정점사이에 간선을 추가한다.
        cin >> capacity[i][E];
        graph[E].push_back(i);
        graph[i].push_back(E);
    }

    for (int i = 0 ; i < M ; i++) { // 소스 정점과 각 서점 정점 사이에 간선을 추가한다.
        cin >> capacity[S][i];
        graph[S].push_back(i);
        graph[i].push_back(S);
    }

    for (int i = 0 ; i < M ; i++) { // 서점과 사람 사이의 간선을 추가한다.
        for (int j = MAX_N ; j< MAX_N+N ; j++) {
            cin >> cost[i][j];
            cost[j][i] = -cost[i][j];
            capacity[i][j] = INF; 
            graph[i].push_back(j);
            graph[j].push_back(i);
        }
    }

    int result = 0; // 최소비용

    while(1) {
        int pre[MAX_V] , dist[MAX_V];
        bool visited[MAX_V] = {0};
        queue<int> Q;

        fill(pre, pre+MAX_V , -1);
        fill(dist , dist+MAX_V , INF);

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
        
        int MIN_Flow = INF; 

        for (int i=E ; i!=S ; i=pre[i]) { // 최소 유량을 최대로 흐를 수 있는 간선을 찾는다.
            MIN_Flow = min(MIN_Flow , capacity[pre[i]][i] - flow[pre[i]][i]);
        }

        for (int i = E ; i!=S ; i=pre[i]) {
            result += MIN_Flow * cost[pre[i]][i]; // 총 비용이 각 간선의 비용만큼 증가.
            flow[pre[i]][i] += MIN_Flow;
            flow[i][pre[i]] -= MIN_Flow;
        }
    }

    cout << result;
}