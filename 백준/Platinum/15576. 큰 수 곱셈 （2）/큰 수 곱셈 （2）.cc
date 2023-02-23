#include <bits/stdc++.h>

using namespace std;
typedef complex<double> cpx; // 복소수
const double PI = acos(-1); // PU 값

#define MAX 200001 // 최대값
int N,M,K,P,T,answer,bit;
string s;
int len,tmp,i,j;

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

    for (int i = 0 ; i < P ; i++)
    {
        c[i] = cpx(round(c[i].real()) , round(c[i].imag()));
    }

    return c;

}

vector<cpx> parse(string &s , int P)
{
    len = s.size()/P;

    if (s.size()%P) 
    {
        len++;
    }

    vector<cpx> ret(len);

    i = 0 ; j = 0 ; tmp = 0;

    if (s.size()%P)
    {
        for (; i < s.size()%P ; i ++)
        {
            tmp = tmp*10 + s[i]-'0';
        }

        ret[j++] = cpx(tmp,0);
    }

    while(i<s.size())
    {
        tmp = 0;
        for (int k = 0 ; k < P;  k++)
        {
            tmp = tmp*10 + s[i+k] - '0';
        }

        i+=P;
        ret[j++] = cpx(tmp,0);
    }

    reverse(ret.begin() , ret.end());
    return ret;
}

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> s;
    if (s=="0")
    {
        cout << 0;
        return 0;
    }

    vector<cpx> a = parse(s,1);

    cin >> s;
    if (s=="0")
    {
        cout << 0;
        return 0;
    }

    vector<cpx> b = parse(s,1);

    vector<cpx> c= multiply(a,b);

    T = 10;

    for (int i = 0 ; i < c.size();  i++)
    {
        if (c[i].real() >= T)
        {
            if (i==c.size()-1)
            {
                c.push_back(cpx((int)c[i].real()/T,0));
            }
            else
            {
                c[i+1] += cpx((int)c[i].real()/T,0);
            }
            c[i] = cpx((int)c[i].real()%T,0);
        }
    }

    reverse(c.begin() , c.end());

    i = 0;
    while(c[i].real() == 0)
    {
        i++;
    }

    for (; i<c.size() ; i++)
    {
        cout << (int)c[i].real();
    }

    return 0;
}