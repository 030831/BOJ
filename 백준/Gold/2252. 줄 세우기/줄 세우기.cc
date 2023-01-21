#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int N , M;
vector<int> indegree;
vector<vector<int>> graph;
queue<int> q;

void input()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M; // 입력

    indegree.assign(N+1, 0); // 입력을 받기 전에는 모든 정점의 진입 차수 : 0

    graph.assign(N+ 1, vector<int>(0, 0));

    for (int i = 0 ; i < M ; i ++)
    {
        int s,e;
        cin >> s >> e;
        graph[s].emplace_back(e); // 2차원 벡터에 값을 할당해준다.
        // 처음 벡터의 크기를 지정하지 않았으므로 emplace_back 을 통해 직접 객체를 생성하고 삽입한다.
        indegree[e]++; // 진입차수를 추가한다. e 를 ++ 한 이유는 s에서 e 로 가는 방향이 증가하였기 때문이다.
    }
}

void topology_sort()
{

    for (int node = 1; node <= N ; node++) // 노드의 1번부터 N 번까지
    {
        if (indegree[node]==0) // 만약 진입차수가 0 이라면
        {
            q.push(node); // q 에다 해당노드를 넣어준다
        }
    }

    for (int i = 0 ; i < N ; i++) // 총 N 번 동안
    {
        /*
        if (q.empty())
        {
            cout << "사이클 발생"
        }
        */

        int node = q.front(); // q 의 가장 앞의 원소를 가져간다. 이는 진입차수가 0 인 노드를 의미한다.
        q.pop(); // 가장 앞의 원소를 지워준다.

        cout << node << " "; // 진입차수가 0 인 노드를 순서대로 출력해준다.

        for (int j = 0; j<graph[node].size(); j++) // 해당 노드에서 갈수있는 모든 노드들에 대해서
        {
            int next_node = graph[node][j]; // 다음으로 방문할 노드를 저장한다.

            if (--indegree[next_node]==0) // 그때 진입차수에 1 을 뺀 값이 0 이라면
            {
                q.push(next_node); // 진입차수가 0 이기 때문에 큐에 원소를 넣어준다.
            }
        }
    }
}

int main()
{
    input();

    topology_sort();
}