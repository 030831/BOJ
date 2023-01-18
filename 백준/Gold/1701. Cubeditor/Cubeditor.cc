#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int maketable(string pattern)
{
    int patternsize = pattern.size();
    vector<int> table (patternsize,0);

    int j=0;

    for (int i = 1; i < patternsize ; i++)
    {
        while (j>0 && pattern[i]!=pattern[j])
        {
            j=table[j-1];
        }

        if (pattern[j]==pattern[i])
        {
            table[i]=++j;
        }
    }

    return *max_element(table.begin(), table.end());
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    string pattern;
    
    getline(cin , pattern);


    int total=0;

    for (int i = 0 ; i < pattern.size() ; i++)
    {
        total = max(total , maketable(pattern.substr(i,pattern.size())));
    }
    cout << total ;
}

/*
주어진 문자열의 두 번이상 나오는 부분문자열 중에서 가장 긴 길이를 출력한다.

실패함수에서 값의 뜻은 접미사와 접두사가 같다는 것. 
즉 실패함수로 만든 table 값이 0 보다 크다면 접두사와 접미사가 같다는 것이므로
부분문자열이 2번 등장했다는 의미이다.

따라서 table 값중 가장 큰 값을 출력한다.
*/