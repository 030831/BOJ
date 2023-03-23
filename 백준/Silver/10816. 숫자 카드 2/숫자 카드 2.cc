#include <bits/stdc++.h>
using namespace std;

int upper_bound(vector<int> &arr , int target , int N)
{
    int start = 0 ;
    int end = N-1;
    int mid;

    while (start<=end)
    {
        mid= (start+end)/2;

        if (arr[mid]>target)
        {
            end = mid-1;
        }
        else if (arr[mid]<=target)
        {
            start = mid+1;
        }
    }
    return end;
}

int lower_bound(vector<int> &arr , int target , int N)
{
    int start = 0 ;
    int end = N-1;
    int mid;

    while (start<=end)
    {
        mid= (start+end)/2;

        if (arr[mid]>=target)
        {
            end = mid-1;
        }
        else if (arr[mid]<target)
        {
            start = mid+1;
        }
    }
    return start;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N , M , K;

    cin >> N;

    vector<int> arr;

    for (int i = 0 ; i < N ; i++)
    {
        cin >> K;
        arr.push_back(K);
    }

    sort(arr.begin() , arr.end());

    cin >> M;
    for (int i = 0 ; i < M ; i++)
    {
        cin >> K;
        cout << max(0 , upper_bound(arr,K , N)-lower_bound(arr,K ,N)+1) << ' ';
    }

}