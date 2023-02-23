#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 1001
int N,Q,K,A,B;
int disjoint[MAX];
vector<pair<int,int>> Query;
int check[MAX];
vector<string> answer;

int Find(int x)
{
    return x==disjoint[x] ? x : disjoint[x] = Find(disjoint[x]);
}
void Union(int a, int b)
{   
    a=Find(a) ; b=Find(b);
    if (a>b)
    {
        disjoint[a]=b;
    }
    else
    {
        disjoint[b]=a;
    }
}
void input()
{
    cin >> N >> Q;

    for (int i = 1 ; i < N; i++)
    {
        cin >> check[i+1];
    }

    for (int i = 0 ; i < N-1+Q ; i++)
    {
        cin >> K;
        if (K==0)
        {
            cin >> A;
            Query.push_back(make_pair(-1,A));
        }
        else
        {
            cin >> A >> B;
            Query.push_back(make_pair(A,B));
        }
    }


}

void solve()
{
    for (int i = 1 ; i <= N ; i++)
    {
        disjoint[i]=i; // 분리집합 초기값은 자기자신을 가르킨다.
    }

    reverse(Query.begin() , Query.end()); // 오프라인쿼리를 위해 역순 정렬

    for (int i = 0 ; i < N-1+Q ; i++)
    {
        if (Query[i].first==-1) // 지우는거라면 연결해준다.
        {
            Union(check[Query[i].second] , Query[i].second);
        }
        else
        {
            if (Find(Query[i].first)==Find(Query[i].second))
            {
                answer.push_back("YES");
            }
            else
            {
                answer.push_back("NO");            
            }
        }
    }
    
    reverse(answer.begin() , answer.end()); // 쿼리를 역순정렬했으므로 정답도 역순으로 뒤집는다.

    for (int i = 0 ; i < answer.size() ; i++)
    {
        cout << answer[i] << "\n";
    }

}
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    input();
    solve();
}