#include <bits/stdc++.h>

using namespace std;
typedef complex<double> cpx; // 복소수
const double PI = acos(-1); // PU 값

#define MAX 1000000 // 최대값
int N,M,K,P,T,answer,bit;
bool prime[MAX+1];
vector<int> check_prime;

void E()
{
    for (int i = 2; i<=MAX; ++i)
    {
        if (!prime[i])
        {
            for (int j = i+i ; j <= MAX ; j+=i)
            {
                prime[j] = true;
            }
        }
    }

    for (int i = 2 ; i<=MAX ; ++i)
    {
        if (!prime[i])
        {
            check_prime.push_back(i);
        }
    }
}

void FFT(vector<cpx> &f , bool inv)
{
    P = f.size();

    for (int i = 1 ,j = 0; i < P ; i++)
    {
        bit = P>>1;

        while (j>=bit)
        {
            j-=bit;
            bit/=2;
        }

        j+=bit;

        if (i<j)
        {
            swap(f[i] , f[j]);
        }
    }

    for (int i = 1 ; i < P ; i <<=1)
    {
        double x = inv ? PI/i : -PI/i;
        cpx w(cos(x) , sin(x));

        for (int j = 0 ; j < P ; j+= i<<1)
        {
            cpx p = cpx(1,0);

            for (int k = 0 ; k < i ; k++)
            {
                cpx tmp = f[i+j+k] * p;
                f[i+j+k] = f[j+k] - tmp;
                f[j+k] +=tmp;
                p *= w;
            }
        }

    }

    if (inv) 
    {
        for (int i = 0 ; i < P ; i ++)
        {
            f[i]/=P;
        }
    }
}

void multiply(vector<cpx> &a , vector<cpx> &b , vector<cpx> &c) 
{

    FFT(a,false);
    FFT(b,false);
     // FFT를 통해 두 다항식을 DFT해 둔다.

    for (int i = 0 ; i < a.size() ; i ++)
    {
        c[i] = a[i]*b[i];
        // DFT한 값들끼리 곱하면 결과 다항식의 DFT값이 된다.
    }
    FFT(c, true);
    //역변환

}

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> T;

    E();

    vector<cpx> a(1<<21) ,b(1<<21) , c(1<<21);
    for (auto C : check_prime)
    {
        a[C] = cpx(1,0);
        if (C*2<=MAX)
        {
            b[C*2]=cpx(1,0);
        }
    }

    multiply(a,b,c);

    while(T--)
    {
        cin >> N;
        cout << round(c[N].real()) << '\n';
    }
}