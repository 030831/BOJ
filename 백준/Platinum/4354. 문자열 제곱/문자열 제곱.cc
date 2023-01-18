#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maketable(string pattern)
{
    int patternsize = pattern.size();

    vector<int> table (patternsize,0);

    int j =0;

    for (int i = 1; i < patternsize ; i++)
    {
        while (j>0 && pattern[i]!=pattern[j])
        {
            j=table[j-1];
        }

        if (pattern[i]==pattern[j])
        {
            table[i]=++j;
        }
    }


    return patternsize - table[table.size()-1];
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    string pattern;

    while (true)
    {
        cin >> pattern;

        if (pattern==".")
        {
            break;
        }

        int answer = maketable(pattern);

        if ( pattern.size()%answer==0)
        {
            cout << pattern.size()/answer << "\n";
        }
        else
        {
            cout <<  1 << "\n";
        }

    }
}

/*
전체 문자열 길이 - 테이블 벡터의 가장 마지막값.

aaaa 일때 4 - 3 = 1

그리고 전체 길이 / 1 = 4

ababab = 6

6-4 = 2

6/2==3

abcd

4-0=4

4/4==1


반례
abababa
.

*/