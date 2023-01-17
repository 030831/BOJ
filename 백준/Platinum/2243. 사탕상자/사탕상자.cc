#include <iostream>
#include <vector>

using namespace std;
int MAX=1000000;

void tree_update(vector<long long>&tree , int node , int start , int end , int index , int value)
{

    if (index<start || index>end)
    {
        return;
    }

    if (start==end)
    {
        tree[node]+=value;
        return;
    }

    tree_update(tree , node*2 , start ,(start+end)/2 , index ,value);
    tree_update(tree ,node*2+1 , (start+end)/2+1 ,end , index ,value);

    tree[node]=tree[node*2]+tree[node*2+1];
}

long long query(vector<long long>&tree , int node , int start , int end ,  int diff)
{

    if (start==end)
    {   
        return start;
    }


    if (diff<=tree[node*2])
    {
        return query(tree , node*2 , start , (start+end)/2  , diff);
    }
    else
    {
        return query(tree , node*2+1 , (start+end)/2+1 , end  , diff-tree[node*2]);
    } 
    

}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    int N;

    cin >> N;

    vector<long long> tree(MAX*4,0);
    
    
    for (int i = 0 ; i  < N;  i ++)
    {
        int A;

        cin >> A;

        if (A==2)
        {
            int index,value;

            cin >> index >> value;
            tree_update(tree , 1 , 1 ,MAX, index , value);

        }
        else
        {
            int want;
            cin >> want;

            int Answer;
            Answer=query(tree,  1,  1 ,MAX , want);

            cout << Answer << "\n";

            tree_update(tree , 1 , 1 , MAX , Answer , -1);

            
        }
    }
}