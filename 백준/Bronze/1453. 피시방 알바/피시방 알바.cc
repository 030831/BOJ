#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N,K;
    int count=0;

    cin >> N;

    vector<int> PC;

    for (int i = 0 ; i < N ; i ++ )
    {
        cin >> K;
        if ( find(PC.begin() , PC.end() , K)!=PC.end())
        {
            count++;
        }
        else
        {
            PC.push_back(K);
        }
    } 

    cout << count ;
}