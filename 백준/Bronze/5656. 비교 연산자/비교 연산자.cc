#include <iostream>

using namespace std;


void Answer_true(int count)
{
    cout << "Case " << count << ": " << "true" << endl;
}

void Answer_false(int count)
{
    cout << "Case " << count << ": " << "false" << endl;
}
int main()
{

    int count = 1;
    int A,B;
    string F;

    while (1)
    {
        cin >> A >> F >> B;

        if (F=="!=")
        {
            if (A!=B)
            {
                Answer_true(count);
            }
            else
            {
                Answer_false(count);
            }
        }
        else if (F=="==")
        {
            if (A==B)
            {
                Answer_true(count);
            }
            else
            {
                Answer_false(count);
            }
        }
        else if (F=="<")
        {
            if (A<B)
            {
                Answer_true(count);
            }
            else
            {
                Answer_false(count);
            }
        }
        else if (F=="<=")
        {
            if (A<=B)
            {
                Answer_true(count);
            }
            else
            {
                Answer_false(count);
            } 
        }
        else if (F==">")
        {
            if (A>B)
            {
                Answer_true(count);
            }
            else
            {
                Answer_false(count);
            }
        }
        else if (F==">=")
        {
            if (A>=B)
            {
                Answer_true(count);
            }
            else
            {
                Answer_false(count);
            } 
        }
        else
        {
            break;
        }
        

        count++;
    }
}