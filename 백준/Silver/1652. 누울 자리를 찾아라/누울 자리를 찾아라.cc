#include <iostream>
#include <vector>

using namespace std;

int main()
{
    //cin.tie(NULL);
    //ios::sync_with_stdio(false);

    int N;

    cin >> N;

    int breath=0 , high = 0;


    vector<string> graph;
    vector<vector<bool>> visit(N);

    fill(visit.begin(), visit.end(), vector<bool>(N, false)); //N은 벡터의 행 크기

    for (int i = 0 ; i < N ; i ++)
    {
        string a;

        cin >> a;

        graph.push_back(a);

    
    }


    for (int i = 0 ; i < N ; i ++ ) 
    {

        for (int j = 0 ; j < N-1 ; j ++)
        {
            if (graph[i][j]=='.' && graph[i][j+1]=='.' && visit[i][j]==false && visit[i][j+1]==false)
            {
                breath++;
                for (int k=j ; k < N ; k++)
                {
                    if (graph[i][k]=='X')
                    {
                        break;
                    }
                    visit[i][k]=true;
                }
            }
        }
    }
    
    fill(visit.begin(), visit.end(), vector<bool>(N, false)); //N은 벡터의 행 크기



    for (int i = 0 ; i < N ; i ++)
    {
        for (int j = 0 ; j < N-1 ; j ++)
        {
            if (graph[j][i]=='.' && graph[j+1][i]=='.' && visit[j][i]==false && visit[j+1][i]==false)
            {
                high++;
                for (int k=j ; k < N ; k++)
                {
                    if (graph[k][i]=='X')
                    {
                        break;
                    }
                    visit[k][i]=true;
                }
            }
        }
    }


    cout << breath << " " << high ;
}