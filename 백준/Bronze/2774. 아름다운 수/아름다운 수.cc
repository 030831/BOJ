#include <iostream>

using namespace std;

int main()
{
    int N;
    string Number;
    int dp_Number;
    int check;

    cin >> N;

    for (int i = 0 ; i < N ; i ++ )
    {
        cin >> Number;

        check=0;
        int dp[10]= {0}; // dp 배열을 처음에 0 으로 초기화한다.


        for (int j = 0 ; j < Number.length() ; j++) 
        {
            dp_Number = Number[j]-'0';

            
            dp[dp_Number]++;
        }

        for (int j = 0 ; j < 10 ; j ++) 
        {

            if (dp[j]!=0)
            {
                check++;
            }
        }

        cout << check << endl;
    }
}