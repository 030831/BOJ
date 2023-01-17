#include <iostream>
#include <algorithm>
#include <vector>
#define INF 1e9
using namespace std;


int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N,X,Y;
    int total=0;

    vector<pair <int , int> > V;

    cin >> N;

    for (int i=0 ; i<N ; i++)
    {
        cin >> X >> Y;
        V.push_back(make_pair(X,Y));
    }

    sort(V.begin() , V.end());

    int left=V[0].first;
    int right=V[0].second;

    for (int i=1 ; i <N ; i++) // 1~N-1
    {
        if (right<V[i].first) // 구간을 벗어난다면
        {
            total+=right-left;
            left=V[i].first;
            right=V[i].second;
        }

        right=max(right, V[i].second);
    }

    total+=right-left;

    cout << total ;

}