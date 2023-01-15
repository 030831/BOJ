#include <iostream>


using namespace std;

int gcd(int a, int b)
{
    int c = a%b;
    while (c!=0)
    {
        a=b;
        b=c;
        c=a%b;
    }

    return b;
}

int lcm(int a, int b)
{
    return (a*b)/gcd(a,b);
}
int main()
{
    int N ; 

    cin >> N;

    int a,b;

    for (int i = 0 ; i < N ; i ++)
    {
        cin >> a >> b;

        cout << lcm(a,b) << " " << gcd(a,b) << endl;

    }
}
