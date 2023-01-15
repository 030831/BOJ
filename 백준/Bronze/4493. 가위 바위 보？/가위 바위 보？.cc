#include <iostream>

using namespace std;

int main()
{
    cin.tie(NULL);

    ios::sync_with_stdio(false);

    int N;

    cin >> N;

    for (int i = 0 ; i < N;  i ++ )
    {
        int K;
        cin >> K;

        int A=0 , B=0;

        for (int j = 0 ; j < K ; j++ )
        {
            char a,b;
            cin >> a >> b;

            if (a=='R' && b=='P')
            {
                B++;
            }
            else if (a=='R' && b=='S')
            {
                A++;
            }
            else if (a=='P' && b=='S')
            {
                B++;
            }
            else if (a=='P' && b=='R')
            {
                A++;
            }
            else if (a=='S' && b=='R')
            {
                B++;
            }
            else if (a=='S' && b=='P')
            {
                A++;
            }
        }

        if (A>B)
        {
            cout << "Player 1\n" ;
        }
        else if (A<B)
        {
            cout << "Player 2\n";
        }
        else
        {
            cout << "TIE\n";
        }
    }
}