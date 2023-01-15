#include <iostream>
#include <string.h>
#include <algorithm>

int arr[26]={0};

using namespace std;


bool Find_PD() // 팰린드롬이 가능한지 체크해주는 함수. 만약 똑같은 문자가 홀수 개수인 경우가 2개이상이라면 불가능하다.
{
    int count=0;
    for (int i = 0 ; i < 26 ; i ++)
    {
        if (arr[i]%2==1)
        {
            count++;
        }
    }

    return count>1;
}
int main()
{
    string name;

    cin >> name;

    string str;

    for (int i = 0 ; i < name.size() ; i++)
    {
        arr[name[i]-'A']++;
    }

    if (Find_PD()) //만약 팰린드롬 을  만들지 못한다면
    {
        cout << "I'm Sorry Hansoo" ;
        return 0;
    }

    for (int i = 0 ; i < 26 ; i++)
    {
        for (int j =0 ; j < arr[i]/2 ; j ++) // 만약 문자가 없다면 0 을 저장했으므로 이 반복문은 실행되지 않는다.
        {
            str+=i+'A'; // 왼쪽부터 절반까지 문자를 넣어준다.
        }
    }
    for (int i = 0 ; i < 26 ; i++)
    {
        if (arr[i]%2==1)
        {
            str+=i+'A'; // 만약 홀수개인 문자가 있으면 넣어준다.
        }
    }

    for (int i = 25 ; i >=0 ; i--)
    {
        for (int j =0 ; j < arr[i]/2 ; j ++)
        {
            str+=i+'A'; // 마지막으로 뒤에서 부터 절반까지 문자를 넣어준다.
        }
    }

    cout << str ;

}