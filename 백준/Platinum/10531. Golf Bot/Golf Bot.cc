#include <bits/stdc++.h>

using namespace std;
typedef complex<double> cpx; // 복소수
const double PI = acos(-1); // PU 값

#define MAX 200001 // 최대값
int N,M,K,P,answer,bit;

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

vector<cpx> multiply(vector<cpx> &a , vector<cpx> &b) 
{
    P = 1;

    while (P<a.size() + b.size())
    {
        P*=2;
    }

    a.resize(P);
    FFT(a,false);
    b.resize(P);
    FFT(b,false);
     // FFT를 통해 두 다항식을 DFT해 둔다.

    vector<cpx> c(P);
    for (int i = 0 ; i < P ; i ++)
    {
        c[i] = a[i]*b[i];
        // DFT한 값들끼리 곱하면 결과 다항식의 DFT값이 된다.
    }
    FFT(c, true);
    //역변환

    return c;

}

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    vector<cpx> A(MAX) , B(MAX);
    vector<int> dist(MAX);

    cin >> N;
    
    for (int i = 0 ; i < N ; i ++) {
        cin >> K;
        A[K] = B[K] = cpx(1,0);
        dist[K] = 1;
    }

    vector<cpx>C = multiply(A,B);

    cin >> M;
    answer = 0;

    for (int i = 0 ; i < M ; i++)
    {
        cin >> K;
        if (dist[K] > 0 || round(C[K].real())>0)
        {
            answer++;
        }
    }

    cout << answer;
}