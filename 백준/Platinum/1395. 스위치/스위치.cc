#include <iostream>
#include <vector>

using namespace std;

void lazy_update(vector<long long>&lazy , vector<long long>&tree , int node , int start , int end )
{

    if (lazy[node]%2==1)  // 껐다 켜서 짝수일때는 의미없다.
    {
        tree[node]=(end-start+1)-tree[node];

        if (start!=end)
        {
            lazy[node*2]+=lazy[node];
            lazy[node*2+1]+=lazy[node];
        }
        lazy[node]=0;
        return;
    }

    
}

void tree_update(vector<long long>&lazy , vector<long long>&tree , int node , int start , int end ,int left , int right  )
{
    lazy_update(lazy , tree , node , start , end);

    if (left>end || right<start)
    {
        return;
    }

    if (left<=start && right>=end)
    {
        tree[node]=(end-start+1)-tree[node]; // 반전 ,(현재 꺼진 스위치의 개수) = (구간의 전체 스위치의 개수) - (현재 켜진 스위치의 개수)
        if (start!=end)
        {
            lazy[node*2]+=1; //스위치 전원을 키는것을 + 1 로 해서 홀짝으로 구분한다.
            lazy[node*2+1]+=1;

        }
        return ;
    }

    tree_update(lazy , tree , node*2 , start , (start+end)/2 , left , right);
    tree_update(lazy , tree , node*2+1 , (start+end)/2+1 , end , left , right);

    tree[node]=tree[node*2]+tree[node*2+1];

}

long long query(vector<long long>&lazy , vector<long long>&tree , int node , int start , int end ,int left , int right)
{

    lazy_update(lazy , tree , node , start , end);

    if (left>end || right<start)
    {
        return 0;
    }

    if (left<=start && right>=end)
    {
        return tree[node];
    }

    return query(lazy, tree , node*2 , start , (start+end)/2 , left , right) + query(lazy , tree , node*2+1 , (start+end)/2+1 , end , left , right);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N , M;

    cin >> N >> M;

    vector<long long> tree(4*N,0);
    vector<long long> lazy(4*N,0);


    while (M--)
    {
        int O,S,T;

        cin >> O >> S >> T;

        if (O==0)
        {
            tree_update(lazy , tree , 1, 0 , N-1 , S-1 , T-1);
        }
        else
        {
            cout << query(lazy , tree , 1, 0,  N-1 , S-1 , T-1) << "\n";
        }
    }
}
