#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    vector<int> check;

    vector<string> name;

    string input_name;
    for (int i = 0 ; i < 5 ; i ++) {
        cin >> input_name;
        name.push_back(input_name);
    }

    for (int i = 0 ; i < 5 ; i ++ ) {
        
        string find_name = name[i];
        if ( find_name.find("FBI")!=string::npos ) {
            check.push_back(i+1);
        }
    }

    if (check.size()==0) {
        cout << "HE GOT AWAY!";
    }
    else {
        for (int i = 0 ; i  < check.size() ; i++) {
            cout << check[i] << " ";
        }
    }

}

