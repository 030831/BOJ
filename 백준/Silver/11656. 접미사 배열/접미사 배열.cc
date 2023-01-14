#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    string a;

    cin >> a;
    

    vector<string> name ;

    for (int i = 0 ; i < a.length() ; i++ ) {
        
        string b ;

        for (int j = i ; j < a.length() ; j ++) {
            b+=a[j];
        }

        name.push_back(b);
    }

    sort(name.begin() , name.end() );

    for (int i = 0 ; i < name.size() ; i++) {
        cout << name[i] << endl;
    }
}