#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define MAX 100001

using namespace std;

vector<vector<int>> SCC;
vector<int> L[MAX];
stack<int> S;

int T,N,M,A,B;
int id,visit[MAX];
bool finished[MAX];
int group[MAX];
bool inDegree[MAX]; //각각의 정점의 진입차수가 몇인지 확인

void query();
void input();
int DFS(int node);

void query()
{
    for (int i = 1 ; i <= N ; i++)
    {
        if (visit[i]==0)
        {
            DFS(i);
        }
    }

    for (int i = 1 ; i <= N ; i++)
    {
        for (int j = 0 ; j < L[i].size() ; j++)
        {
            int P = L[i][j];
            if (group[i]!=group[P])
            {
                inDegree[group[P]]=true;
            }
        }
    }

    int total = 0;

    for (int i = 1; i <= SCC.size(); i++)
    {
        if (!inDegree[i])
        {
            total++;
        }
    }

    cout << total << "\n";
}

int DFS(int node)
{
    visit[node]=++id;

    S.push(node);
    
    int parent=visit[node];

    for (int i = 0 ; i < L[node].size() ; i++)
    {
        int next_node = L[node][i];

        if (visit[next_node]==0)
        {
            parent=min(parent,DFS(next_node));
        }
        else if (!finished[next_node])
        {
            parent=min(parent,visit[next_node]);
        }
    }

    if (parent==visit[node])
    {
        vector<int> small_scc;

        while (1)
        {
            int K = S.top();
            S.pop();

            small_scc.push_back(K);
            finished[K]=true;
            group[K]=SCC.size()+1;

            if (K==node)
            {
                break;
            }
        }

        SCC.push_back(small_scc);
    }

    return parent;

}

void input()
{
    cin >> T;

    while (T--)
    {
        cin >> N >> M;

        fill(visit,visit+MAX,0);
        fill(finished,finished+MAX,0);
        fill(inDegree,inDegree+MAX,0);
        SCC.clear();

        for (int i = 1 ; i <= N ; i++)
        {
            L[i].clear();
        }
        
        for (int i = 0 ; i < M ; i++)
        {
            cin >> A >> B;

            L[A].push_back(B);
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