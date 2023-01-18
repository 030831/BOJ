#include <iostream>
#include <vector>

using namespace std;
vector<int> answer;

vector<int> maketable(string pattern) // 실패함수.
{

    int patternsize = pattern.size();

    vector<int> table(patternsize , 0);

    int j = 0;

    for (int i =1 ; i < patternsize ; i++)
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

    return table;
}

void KMP(string pattern , string parent)
{
    vector<int> table=maketable(pattern);

    int patternsize=pattern.size();
    int parentsize=parent.size();

    int j=0;

    for (int i = 0; i < parentsize ; i++)
    {
        while (j>0 && parent[i]!=pattern[j])
        {
            j=table[j-1];
        }

        if (parent[i]==pattern[j])
        {
            if (j==patternsize-1)
            {
                answer.push_back(i-patternsize+2);
                j=table[j];
            }
            else
            {
                j++;
            }
        }
    }
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    string parent , pattern;

    getline(cin , parent);
    getline(cin , pattern);

    KMP(pattern , parent);

    cout << answer.size() << "\n";

    for (int i = 0 ; i < answer.size() ; i++)
    {
        cout << answer[i] << " ";
    }

    return 0;   
}