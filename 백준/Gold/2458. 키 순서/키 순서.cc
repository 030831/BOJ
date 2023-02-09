#include <iostream>


using namespace std;

int graph[501][501];
int INF=1e9;
int N,M,s,e,check,total;

int Floyd_Warshall()
{
    for (int k = 1;  k <=N ; k++)
    {
        for (int i = 1 ; i<=N ; i++)
        {
            for (int j = 1;  j<=N ; j++)
            {
                graph[i][j]=min(graph[i][j] , graph[i][k]+graph[k][j]-1);
            }
        }
    }

    total = 0;

    for (int i = 1 ; i <=N ; i++)
    {
        check = 0;
        for (int j = 1 ; j<=N ; j++) 
        {
            if (graph[i][j]==1 || graph[j][i]==1)
            {
                check++;
            }
        }

        if (check==N-1)
        {
            total++;
        }
    }

    return total;
}

void input()
{
    cin >> N >> M;
    
    for (int i = 1 ; i<=N ; i++)
    {
        for (int j = 1 ; j<=N ; j++)
        {
            graph[i][j]=INF;
        }
    }
    for (int i = 0 ; i < M ; i++)
    {
        cin >> s >> e;
        graph[s][e]=1;
    }

}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    input();

    cout << Floyd_Warshall();

}