#include <bits/stdc++.h>
using namespace std;

int T,N,M;
int graph[501];
bool visited[501][501];
int indegree[501];


/*
2차원 visited 배열을 통해서 위치가 바뀐 두 지점을 boolean 값으로 체크해주면서 위상정렬을 한다.
*/
void query()
{
    queue<int> q;

    for (int i = 1 ; i<=N; i++)
    {
        if (indegree[i]==0)
        {
            q.push(i);
        }
    }

    vector<int> answer; // 위상정렬의 경로를 담는다.

    for (int i = 0 ; i < N ; i++)
    {
        if (q.empty())
        {
            break;
        }

        int node = q.front();
        q.pop();
        indegree[node]--;
        answer.push_back(node);

        for (int j =1 ; j<=N ; j++)
        {
            if (visited[node][j])
            {
                if (--indegree[j]==0)
                {
                    q.push(j);
                }
            }
        }
    }

    if (answer.size()==N)
    {
        for (auto node : answer)
        {
            cout << node << " ";
        }
        cout << "\n";
    }
    else
    {
        cout << "IMPOSSIBLE" << '\n';
    }
}

void input()
{
    cin >> T;

    while(T--)
    {
        memset(indegree,0,sizeof(indegree));
        memset(visited,false,sizeof(visited));

        cin >> N;

        for (int i = 1 ; i <=N ; i++)
        {
            cin >> graph[i];
        }

        for (int i = 1 ; i <=N ; i++)
        {
            for (int j=i+1 ; j <=N ; j++)
            {
                visited[graph[i]][graph[j]]=true;
                indegree[graph[j]]++;
            }
        }

        cin >> M;

        for (int i = 0 ; i < M ; i++)
        {
            int a,b;
            cin >> a >> b;

            if (visited[a][b])
            {
                visited[a][b]=false;
                visited[b][a]=true; // 순서 변경.
                indegree[a]++;
                indegree[b]--;
            }
            else
            {
                visited[b][a]=false;
                visited[a][b]=true; // 순서변경
                indegree[a]--;
                indegree[b]++;
            }
            
        }

        query();

    }

}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    input();
}