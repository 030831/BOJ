#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define M 401
#define INF 100000000
#define MAX 802


int N,P;
int capacity[MAX][MAX];
int flow[MAX][MAX];
int parent[MAX];
int START,END,node,result,use_flow;
vector<int> graph[MAX];



void input() 
{
    cin >> N >> P;

    for (int i = 1 ; i <= N ; i++) {
        graph[i].push_back(M+i);
        graph[M+i].push_back(i);
        capacity[i][M+i]=1;
    }
    for (int i = 0 ; i < P ; i++) {
        cin >> START >> END;
        capacity[START+M][END] =1;
        graph[START+M].push_back(END);
        graph[END].push_back(START+M);

        capacity[END+M][START] = 1;
        graph[START].push_back(END+M);
        graph[END+M].push_back(START);
    }
}

int MAX_FLOW(int source , int sink) {

    result = 0;

    while (1) {
        fill(parent , parent+MAX , -1);
        queue<int> Q;
        Q.push(source);

        while (!Q.empty()) {
            node = Q.front();
            Q.pop();

            for (int next_node : graph[node]) {
                if (parent[next_node]==-1 && capacity[node][next_node] - flow[node][next_node] > 0) {
                    Q.push(next_node);
                    parent[next_node] = node;

                    if (next_node == sink) {
                        break;
                    }
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

    cout << MAX_FLOW(M+1,2);
}