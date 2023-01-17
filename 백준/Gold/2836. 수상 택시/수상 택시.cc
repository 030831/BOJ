#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int N , M;

    cin >> N >> M;

    vector<pair<long long, long long>> V;

    for (int i = 0 ; i < N ; i ++)
    {
        long long A,B;
        cin >> A >> B;

        if (A>B)
        {
            V.push_back(make_pair(B,A));
        }
    }

    sort(V.begin() , V.end());

    long long left=V[0].first; 
    long long right=V[0].second;
    long long total = 0;

    for (int i = 1 ; i < V.size() ; i ++)  
    {
        if (right<V[i].first) // 구간을 벗어난다면
        {
            total+=right-left;
            right=V[i].second;
            left=V[i].first;
        }

        right=max(right , V[i].second);
    }

    total+=right-left;

    cout << M+total*2;
}