#include <bits/stdc++.h>

using namespace std;

int binary_search(vector<int> &arr , int M)
{
    int start = 0;
    int end = 0;

    for (auto x : arr) {
        end +=x;
        start=max(start,x);
    }


    while (start <= end) {
        int mid = (start+end)/2;
        int ans = 0 ;
        int count = 0;

        for (int i = 1 ; i<arr.size() ; i++)
        {
            ans += arr[i-1];

            if (ans + arr[i] > mid )
            {
                count +=1;
                ans = 0;
            }
        }

        if (count>=M)
        {
            start = mid+1;
        }
        else
        {
            end = mid-1;
        }
    }
    return start;
}

int main()
{
    int N, M , K;

    cin >> N >> M;

    vector<int> arr;

    for (int i = 0 ; i < N ; i++) {
        cin >> K;
        arr.push_back(K);
    }

    cout << binary_search(arr,M);
}