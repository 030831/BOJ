#include <iostream>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;

    cin >> N;

    int a=0 , b=0;

    int c,d;

    for (int i = 0 ; i < N ; i ++)
    {
        cin >> c >> d;
        if (c>d)
        {
            a++;
        }
        else if (c<d)
        {
            b++;
        }
    }

    cout << a << " " << b;
}