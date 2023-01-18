#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int total=0;


vector<int> maketable(string pattern)
{
    int patternsize = pattern.size();

    vector<int> table(patternsize , 0);

    int j = 0 ;

    for (int i = 1;  i < patternsize ; i++)
    {
        while( j > 0 && pattern[i]!=pattern[j])
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

void KMP(string parent ,string pattern)
{
    int parentsize = parent.size();
    int patternsize= pattern.size();

    vector<int> table = maketable(pattern);

    int j = 0;

    for (int i = 0 ; i < parentsize ; i++)
    {
        while(j>0 && parent[i]!=pattern[j])
        {
            j=table[j-1];
        }

        if (parent[i]==pattern[j])
        {
            if (j==patternsize-1)
            {
                total++;
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

    int N;

    cin >> N;
    cin.ignore(); // 정수 입력받았으면 줄바꿈 문자 제거해야함.

    string parent2;
    string pattern;

    getline(cin , parent2);
    getline(cin , pattern);

    parent2.erase(remove(parent2.begin() , parent2.end(), ' ') , parent2.end());
    pattern.erase(remove(pattern.begin() , pattern.end() , ' ') , pattern.end());

    string parent;

    parent += parent2;
    parent += parent2;

    parent=parent.substr(0, parent.size()-1);

    KMP(parent , pattern);


    cout << "1/" << N/total;

}