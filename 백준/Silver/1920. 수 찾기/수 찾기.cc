#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;
void binary_search(vector<long long> &a , long long w)
{
    int start = 0;
    int end = a.size()-1;

    int mid;
    while (start <= end)
    {
        mid = (start + end) / 2;
        if (a[mid] > w)
        {
            end = mid-1;
        }
        else if (a[mid] < w)
        {
            start = mid+1;
        }
        else
        {
            cout << 1 << "\n";
            return;
        }
    }
    cout << 0 << "\n";

}
int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    long long n,m,w;
    vector<long long> a;
    vector<long long> k;
    cin >> n;
    for (int i = 0; i < n; i++)
    {

        cin >> w;
        a.push_back(w);
    }

    sort(a.begin() , a.end());

    cin >> m;

    for (int i = 0; i < m; i++)
    {
        cin >> w;
        binary_search(a , w);
    }

}
