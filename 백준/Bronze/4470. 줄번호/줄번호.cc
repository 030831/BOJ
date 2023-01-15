#include <iostream>

using namespace std;

int main()
{

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;

    cin >> N;
    cin.ignore(); // \n 을 지운다.
    
    for (int i = 1 ; i <= N ; i ++)
    {
        string text;

        getline(cin , text);

        cout << i << ". " << text << "\n";
    }


}