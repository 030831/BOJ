#include <iostream>
#include <queue>
#include <vector>
#include <string.h>

using namespace std;

#define MAX_NODE 52 // 전체 알파벳 개수 , 소문자와 대문자
#define INF 1e9 // 최대유량 비교시 사용

int capacity[MAX_NODE][MAX_NODE]; // 용량배열
int flow[MAX_NODE][MAX_NODE]; // 유량 배열
int visited[MAX_NODE]; //방문처리 배열

vector<int> graph[MAX_NODE]; // BFS 탐색시 인접한 노드 탐색을 하는 배열

int MAX_Flow; // 최대유량을 저장할 변수


int stoi(char c) { // 문자를 숫자로 바꾸는 함수
    
    if (c<='Z') {
        return c-'A'; // 대문자라면 0~25범위값으로 반환한다.
    }
    return c-'a'+26; // 소문자라면 26~51의 범위값으로 반환한다.
}


int Network_flow(int source , int sink) { // BFS 를 사용해 source 에서 sink 로의 최단경로 탐색

    while(1) { // source 에서 sink 까지의 증가경로가 없을때까지 반복한다.
        
        memset(visited , -1 , sizeof(visited)); // 방문처리 배열을 -1 로 초기화한다.

        queue<int> q; // BFS 탐색에 쓸 큐 선언
        q.push(source); // 큐에 정점 하나를 삽입한다.

        while(!q.empty()) { // 큐의 원소가 없을때까지
            int node = q.front(); 
            q.pop();

            for (int i = 0 ; i < graph[node].size() ; i++) {
                int next_node = graph[node][i] ; 

                if ( (capacity[node][next_node]-flow[node][next_node]>0) && (visited[next_node]==-1)) {
                    // 인접노드 경로에 잔여용량이 남아있고 아직 방문하지 않았다면
                    q.push(next_node);
                    visited[next_node] = node; // 이후 역추적 하기 위해 다음노드 인덱스에 현재노드값을 저장한다.


                    if (next_node == sink) {
                        break; // sink 노드를 찾았다면 종료
                    }
                }
            }

            if (visited[sink]!=-1) {
                break; // sink 노드를 방문했다면 종료
            }
        }

        if (visited[sink]==-1) {
            break; // BFS 탐색이 끝나도 sink 로 가는 경로가 없다면 종료 
        }

        int check_max_flow = INF; // 최대유량체크변수
        int residual_capacity; // 남은 용량

        for (int i = sink ; i!=source ; i=visited[i]) { // 방문노드를 역추적한다. 그리고 최대유량중 최소값을 찾는다.
            residual_capacity = capacity[visited[i]][i] - flow[visited[i]][i];
            // visit[i] = next_node ;  i = node 
            
            check_max_flow = min(check_max_flow , residual_capacity) ;
        }

        for (int i = sink ; i!=source ; i=visited[i]) { //최소 유량을 흘러보낸다.
            flow[visited[i]][i] += check_max_flow;
            flow[i][visited[i]] -= check_max_flow; // 역방향 간선에는 음수를 추가한다.
        }

        MAX_Flow += check_max_flow; // 최대 유량을 저장할 변수에 최소유량값을 더해준다.
    }

    return MAX_Flow;
} 

void input() {
    int E; // 간선의 개수
    cin >> E;

    char start,end; // 간선
    int input_capacity; // 간선의 용량

    for (int i = 0 ; i < E ; i++){
        cin >> start >> end >> input_capacity; 

        int stoi_start = stoi(start);
        int stoi_end = stoi(end);

        graph[stoi_start].push_back(stoi_end);
        graph[stoi_end].push_back(stoi_start); // 단방향 이라도 양방향으로 만들어 준다.

        capacity[stoi_start][stoi_end]+=input_capacity;
        capacity[stoi_end][stoi_start]+=input_capacity; // 양방향으로 용량 할당.
    }
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    input();

    cout << Network_flow(stoi('A') , stoi('Z')); // A 부터 Z 까지 최대유량 탐색
}