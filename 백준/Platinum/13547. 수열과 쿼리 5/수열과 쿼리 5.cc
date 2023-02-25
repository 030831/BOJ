#include <bits/stdc++.h>

using namespace std;

const int MAX =  1000001;

int sqrtN;
int N,M;
int L[MAX],cnt[MAX+1],result[MAX];
int Left , Right , sqrtA , sqrtB , l , r , sum;

struct Query
{
    int l,r,idx;
};


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

vector<Query> Q;
void input()
{
    cin >> N;
    sqrtN = sqrt(N); // 평방 분할.
    for (int i = 0 ; i < N ; i++)
    {
        cin >> L[i];
    }

    cin >> M;

    for (int i = 0 ; i < M ; i++)
    {
        cin >> Left >> Right;
        Q.push_back({Left-1 , Right , i});
    }
}

void Mo_s()
{
    sort(Q.begin() , Q.end() ,compare);

    l=Q[0].l; r = Q[0].r;

    for (int i = l ; i < r ; i++)
    {
        if (cnt[L[i]]++ == 0)
        {
            sum++;
        }
    }

    result[Q[0].idx] = sum;

    for (int i = 1 ; i < M ; i++)
    {
        while(Q[i].l < l) if (cnt[L[--l]] ++ ==  0) sum++; // 왼쪽 구간 확대시 새로운 값이 나오면 증가 , 왼쪽구간은 오른쪽으로 가는것이 확대
        while(Q[i].l > l) if (--cnt[L[l++]] == 0) sum--; // 왼쪽 구간 축소시 새로운 값이 나오면 감소
        while(Q[i].r > r) if (cnt[L[r++]]++ == 0) sum++; // 오른쪽 구간 확대시 새로운 값이 나오면 증가
        while(Q[i].r < r) if (--cnt[L[--r]] == 0) sum--; // 오른쪽 구간 축소시 새로운 값이 나오면 감소

        result[Q[i].idx] = sum;
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