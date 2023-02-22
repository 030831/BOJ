#include <iostream>
#include <vector>
#define MAX 1001

using namespace std;

vector<int> graph[MAX];
int flow[MAX];
bool visited[MAX];
int N,M,K,T;
int result;

bool DFS(int node) 
{
    for (int i = 0 ; i < graph[node].size() ; i++) {
        int next_node = graph[node][i];

        if (visited[next_node]) {
            continue;
        }

        visited[next_node] = true;

        if (flow[next_node] == 0 || DFS(flow[next_node])) {
            flow[next_node] = node;
            return true;
        }
    }
    return false;
}

void input()
{
    cin >> N >> M;

    for (int i = 0 ; i < N ; i++) {
        cin >> K;
        for (int j = 0 ; j < K ; j++) {
            cin >> T;
            graph[i+1].push_back(T);
        }
    }
}
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    input();

    result = 0;
    for (int i = 1 ; i <= N ; i ++) {
        fill(visited, visited+MAX , false);
        if (DFS(i)) {
            result ++;
        }
    }

    cout << result;
}