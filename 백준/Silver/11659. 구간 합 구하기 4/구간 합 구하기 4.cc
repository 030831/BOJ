#include <bits/stdc++.h>

using namespace std;


const int MAX = 100001;
int sqrtN;
int N,M,K,Left,Right;
int L[MAX],result[MAX];
int sqrtA,sqrtB,Left_Pointer,Right_Pointer,Query_Left,Query_Right;
int sum,idx;

struct Query
{
    int l,r,index;
};

vector<Query> Q;

bool compare(Query a , Query b) // (s/√N, e) 순으로 오름차순 정렬
{
    sqrtA = a.l / sqrtN;
    sqrtB = b.l / sqrtN;
    
    if (sqrtA != sqrtB)
    {
        return sqrtA<sqrtB;
    }
    return a.r < b.r;
}
void input()
{
    cin >> N >> M;

    for (int i = 0 ; i < N ; i++)
    {
        cin >> L[i];
    }

    for (int i = 0 ; i < M ; i++)
    {
        cin >> Left >> Right;
        Q.push_back({Left-1 , Right , i}); // Left-1
    }

}

void Mo_s()
{
    sqrtN = sqrt(N);

    sort(Q.begin() , Q.end() , compare);

    Left_Pointer = Q[0].l;
    Right_Pointer = Q[0].r;
    sum = 0;

    // 첫 번째에 위치한 쿼리의 결과는 손수 구함
    for (int i = Left_Pointer ; i < Right_Pointer ; i++)
    {
        sum+=L[i];
    }

    result[Q[0].index]=sum;

    for (int i = 1 ; i < M ; i++)
    {
        while(Q[i].l < Left_Pointer) // 이전 쿼리보다 s가 작을 경우 왼쪽으로 구간을 확장하며 더함
        {
            sum+=L[--Left_Pointer];
        }

        while(Right_Pointer<Q[i].r) // 이전 쿼리보다 e가 클 경우 오른쪽으로 구간을 확장하며 더함
        {
            sum+=L[Right_Pointer++];
        }
        
        while(Q[i].l > Left_Pointer) // 이전 쿼리보다 s가 클 경우 구간을 왼쪽으로부터 축소하며 뺌
        {
            sum-=L[Left_Pointer++];
        }

        while(Right_Pointer>Q[i].r) // 이전 쿼리보다 e가 작을 경우 구간을 오른쪽으로부터 축소하며 뺌
        {
            sum-=L[--Right_Pointer];
        }

        result[Q[i].index] = sum;
    }
    for (int i = 0 ; i < M ; i++)
    {
        cout << result[i] << '\n';
    }
}
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    input();
    Mo_s();
}