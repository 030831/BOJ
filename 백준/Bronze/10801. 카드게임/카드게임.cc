#include <iostream>
#include <vector>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    vector<int> A;
    vector<int> B;

    int A_count=0 , B_count=0 ;
    for (int i = 0 ; i < 10 ; i ++)
    {
        int N;
        cin >> N;

        A.push_back(N);
    }
    for (int i = 0 ; i < 10 ; i ++)
    {
        int N;
        cin >> N;

        B.push_back(N);
    }

    for (int i = 0 ; i < 10 ; i ++)
    {
        if (A[i]<B[i])
        {
            B_count++;
        }
        else if (A[i]>B[i])
        {
            A_count++;
        }
    }

    if (A_count>B_count)
    {
        cout << "A";
    }
    else if (A_count <B_count)
    {
        cout << "B";
    }
    else 
    {
        cout << "D";
    }
}