#include <iostream>
#include <vector>

using namespace std;

vector<int> maketable(string pattern)
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

    return table;
}

int main()
{

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;

    cin >> N;

    cin.ignore();

    string pattern;

    getline(cin , pattern);

    vector<int> table = maketable(pattern);

    cout << N-table[table.size()-1];

}

/*
문자열의 마지막이 접두사와 중복된 채로 끝난다면 해당 중복 문자열의 길이만큼 광고 문자열을 감소시킬 수 있다.
10
abcaabcaab

answer = 4

5
aaaaa

answer = 1

7
abaabab -ababa

answer=5

*/