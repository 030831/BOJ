#include <iostream>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;

    cin >> N;

    if (N<=3)
    {
        cout << 0;
    }
    else
    {
        int A=1;

        for (int i=N ; i>=N-3 ; i--)
        {
            A*=i;
        }

        A/=24;

        cout << A ;
    }
}