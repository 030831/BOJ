#include <iostream>
#include <queue>

using namespace std;

int graph[101][101];
int N,M;
int visit[101];
queue<int> q;

void BFS(int start)
{
    q.push(start);

    visit[start]++;

    while (!q.empty())
    {
        int node = q.front();
        q.pop();

        for (int i = 1 ; i <= N ; i++)
        {
            if (graph[node][i]!=1 || visit[i]>=0)
            {
                continue;
            }

            q.push(i);
            visit[i]=visit[node]+1;
        }
    }
}
int main()
{
    cin >> N >> M;

    for (int i = 0 ; i < M ; i ++)
    {
        int a, b;
        cin >> a >> b;
        graph[a][b]=1;
        graph[b][a]=1;
    
    }

    int MIN=1000000000 ,ans;


    for (int i = 1; i <=N ; i ++)
    {
        for (int i = 1; i <=N ; i++)
        {
            visit[i]=-1;
        }
        BFS(i);
        int SUM=0;

        for (int i = 1 ; i<=N ; i ++)
        {
            SUM+=visit[i];

        }

        if (SUM<MIN)
        {
            MIN=SUM;
            ans=i;
        }
    }

    cout << ans;


}