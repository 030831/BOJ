#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;

    int a,b;
    string Affine;

    for (int i = 0 ; i < N ; i ++ ) 
    {
        cin >> a >> b ;
        cin >> Affine;

        for (int j = 0 ; j<Affine.length() ; j++) 
        {
            cout << (char)( (((int)Affine[j]-65)*a+b)%26 + 65);
        }
        
        cout << "\n";
    }
}