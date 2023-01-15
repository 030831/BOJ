#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{

    int N;
    string car;
    char spell;

    cin >> N;

    int totalleft;
    int totalright;
    int P;

    for (int i = 0 ; i < N ; i ++) {

        cin >> car;

        totalleft=0;
        totalright=0;

        for (int j = 0 ; j < 3 ; j ++) {
            spell = car[j];
            
            P=1;
            for (int k = 0 ; k <  2- j ; k++) {
                P*=26;
            }
            totalleft += ((int)(spell)-65)*P;

        }
    


        for (int j =4 ; j <8 ; j++) {

            P=car[j]-'0'; // 0~9 문자인 숫자를 int 형 숫자로 바꿔준다.

            for (int k = 0 ; k < 7-j ; k++) {
                P*=10;
            }
            totalright+=P;
        }

        

        if ( abs(totalleft-totalright)<=100){
            cout << "nice" << endl;
        }
        else {
            cout << "not nice" << endl;
        }
    }
}
