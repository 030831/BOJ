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

