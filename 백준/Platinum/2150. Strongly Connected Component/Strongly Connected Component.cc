#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define MAX 10001

using namespace std;

int id,visit[MAX];
int V,E,A,B;
bool finished[MAX];
vector<int> L[MAX];
vector<vector<int>> SCC;
stack<int> S;

void query();
void input();
int DFS(int node);
bool cmp(vector<int> &v1, vector<int> &v2);

bool cmp(vector<int> &v1, vector<int> &v2)
{
    return v1[0]<v2[0];
}

void query()
{

    for (int i =  1 ; i <= V ; i++)
    {
        if (visit[i]==0)
        {
            DFS(i);
        }
    }

    
    cout << SCC.size() << "\n";

    for (int i = 0 ; i < SCC.size() ; i++)
    {
        sort(SCC[i].begin() , SCC[i].end());
    }

    sort(SCC.begin() , SCC.end(), cmp);

    for (int i = 0 ; i < SCC.size() ; i++)
    {
        for (int j = 0 ; j < SCC[i].size() ; j++)
        {
            cout << SCC[i][j] << " ";
        }
        cout << "-1\n" ;
    }
}

int DFS(int node)
{
    visit[node]=++id; // 노드마다 고유한 번호를 할당한다.
    S.push(node);

    int parent=visit[node];

    for (int i =0 ; i < L[node].size() ; i++)
    {
        int next_node = L[node][i];

        if (visit[next_node]==0)
        {
            parent=min(parent , DFS(next_node)); // 강한연결요소끼리 묶는다.
        }
        else if (!finished[next_node])
        {
            parent=min(parent,visit[next_node]);
        }
    }

    if (parent==visit[node])  // 부모노드가 자기 자신인 경우.
    {
        vector<int> small_scc;

        while (1)
        {
            int K=S.top();
            S.pop();

            small_scc.push_back(K);
            
            finished[K]=true;

            if (K==node)
            {
                break;
            }
        }

        SCC.push_back(small_scc); // 강한연결요소 부분집합을 넣어준다.
    }

    return parent; // 자신의 부모값을 반환한다.
}

void input()
{
    cin >> V >> E;

    for (int i = 0 ; i < E ; i++)
    {
        cin >> A >> B;
        L[A].push_back(B);
    }
}
int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    input();
    query();
}