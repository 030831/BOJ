#include <iostream>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int month , day;

    cin >> month >> day;

    if (month<=1)
    {
        cout << "Before";
    }
    else if (month==2)
    {
        if (day<18)
        {
            cout << "Before";
        }
        else if (day==18)
        {
            cout << "Special";
        }
        else
        {
            cout << "After";
        }
    }
    else
    {
        cout << "After";
    }
}