#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define M 401
#define INF 100000000

int N,P;
int capacity[M][M];
int flow[M][M];
int parent[M];
int START,END,node,result,use_flow;
vector<int> graph[M];



void input() 
{
    cin >> N >> P;

    for (int i = 0 ; i < P ; i++) {
        cin >> START >> END;
        capacity[START][END] =1;
        graph[START].push_back(END);
        graph[END].push_back(START);
    }
}

int MAX_FLOW(int source , int sink) {

    result = 0;

    while (1) {
        fill(parent , parent+M , -1);
        queue<int> Q;
        Q.push(source);

        while (!Q.empty()) {
            node = Q.front();
            Q.pop();

            for (int next_node : graph[node]) {
                if (parent[next_node]==-1 && capacity[node][next_node] - flow[node][next_node] > 0) {
                    Q.push(next_node);
                    parent[next_node] = node;
                }
            }
        }

        if (parent[sink] == -1) { // 모든 경로를 다 찾았다면
            break;
        }
        use_flow = INF;
        for (int i = sink ; i!=source ; i=parent[i]) {
            use_flow = min(use_flow , capacity[parent[i]][i] - flow[parent[i]][i]) ;
        }

        for (int i = sink ; i!=source  ; i=parent[i]) {
            flow[parent[i]][i] += use_flow;
            flow[i][parent[i]] -= use_flow;
        }

        result += use_flow;
        
    }

    return result;

}
int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    input();

    cout << MAX_FLOW(1,2);
}