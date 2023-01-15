#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    cin.tie(NULL);

    ios::sync_with_stdio(false);

    int N;
    int total=0;
    cin >> N;


    for (int i = 0 ; i < N ; i ++)
    {
        int a,b,c,d;
        cin >> a >> b >> c >> d;
        int dp[7]={0};
    
        dp[a]++;
        dp[b]++;
        dp[c]++;
        dp[d]++;


        for (int j = 1 ; j < 7 ; j ++)
        {
            if (dp[j]==4)
            {
                total = max(total , 50000+j*5000);
            
            }
            if (dp[j]==3)
            {
                total = max(total , 10000 + j*1000);
            }
            if (dp[j]==2)
            {
                bool check=false;
                for (int k = j+1 ; k < 7 ; k++)
                {
                    if (dp[k]==2)
                    {
                        check=true;
                        total = max(total , 2000+j*500+k*500);
                    }
                }
                if (check==false)
                {
                    total = max(total , 1000+j*100);

                }

            } 
        }


        bool check=false;
        int Index=0;

        for (int j = 1 ; j < 7 ; j ++)
        {
            if (dp[j]==1)
            {
                Index=j*100;
            }
            else if (dp[j]>1)
            {
                check=true;
            }
        }

        if (check==false)
        {
            total = max(total ,Index);
        }

    

    }
    cout << total ;
}