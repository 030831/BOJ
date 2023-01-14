#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    string a;

    cin >> a;

    vector<string> name ;

    string b;

    for (int i = 0 ; i < a.length() ; i++ ) {

        b=a.substr(i,a.length()-i);    
        name.push_back(b);
    }

    sort(name.begin() , name.end() );

    for (int i = 0 ; i < name.size() ; i++) {
        cout << name[i] << endl;
    }
}