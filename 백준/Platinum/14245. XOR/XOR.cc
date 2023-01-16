#include <iostream>
#include <vector>

using namespace std;

void init(vector<long long> &L , vector<long long>&tree,  int node , int start , int end)
{
    if (start==end)
    {
        tree[node]=L[start];
        return;
    }

    init(L , tree , node*2 , start , (start+end)/2);
    init(L , tree , node*2+1 , (start+end)/2+1 , end);

    tree[node]=tree[node*2]^tree[node*2+1];

}


void lazy_update(vector<long long>&lazy , vector<long long>&tree , int node , int start , int end )
{

    if (lazy[node]!=0)
    {
        tree[node]^=(end-start+1)*lazy[node];

        if (start!=end)
        {
            lazy[node*2]^=lazy[node];
            lazy[node*2+1]^=lazy[node];
        }

        lazy[node]=0;
    }

}

void tree_update(vector<long long>&lazy , vector<long long>&tree , int node , int start , int end , int left ,int right , long long diff)
{
    lazy_update(lazy , tree , node , start , end);

    if (left>end || right<start)
    {
        return;
    }

    if (left<=start && right>=end)
    {
        tree[node]^=(end-start+1)*diff;

        if (start!=end)
        {
            lazy[node*2]^=diff;
            lazy[node*2+1]^=diff;
        }

        return;
    }

    tree_update(lazy,tree, node*2 , start , (start+end)/2 , left , right , diff);
    tree_update(lazy, tree, node*2+1,  (start+end)/2+1 , end , left , right , diff);
    
    tree[node]=tree[node*2]^tree[node*2+1];
}

long long query(vector<long long>&lazy  , vector<long long>&tree , int node , int start , int end , int index)
{
    lazy_update(lazy , tree , node , start , end);

    if (index<start || index>end)
    {
        return 0;
    }

    if (start==end)
    {
        return tree[node];
    }

    return query(lazy,tree , node*2 , start ,(start+end)/2 , index) ^ query(lazy, tree , node*2+1,  (start+end)/2+1 , end  , index);
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N ;

    cin >> N;

    vector<long long> L(N);
    vector<long long> tree(4*N);
    vector<long long> lazy(4*N);

    for (int i = 0 ; i < N ; i ++)
    {
        cin >> L[i];
    }

    init(L,tree,1,0,N-1); // 트리 초기화.

    int M ;

    cin >> M;



    while (M--)
    {
        int Q;

        cin >> Q;

        if (Q==1)
        {
            int a,b,c;

            cin >> a >> b >> c;

            tree_update(lazy ,tree , 1, 0 , N-1 , a , b , c);

        }
        else
        {
            int Input_Index;

            cin >> Input_Index;


            cout << query(lazy ,tree , 1 , 0 , N-1 , Input_Index) << "\n";

        }
    }
}