#include <iostream>

using namespace std;

int main()
{

    int N,M;

    cin >> N;

    
    while (1)
    {
        cin >> M ;

        if (M==0) 
        {
            break;
        }
        
        if (M%N==0)
        {
            cout << M << " is a multiple of " << N << "." << endl;
        }
        else
        {
            cout << M << " is NOT a multiple of " << N << "." << endl;
        }
    }
}