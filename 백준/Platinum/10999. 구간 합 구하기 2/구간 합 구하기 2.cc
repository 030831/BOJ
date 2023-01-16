#include <iostream>
#include <vector>

using namespace std;


void init(vector<long long>&L, vector<long long>&tree , int node , int start , int end)
{
    if (start==end)
    {
        tree[node]=L[start];
        return;
    }

    init(L , tree , node*2 , start , (start+end)/2 );
    init(L , tree , node*2+1 , (start+end)/2+1 , end );

    tree[node]=tree[node*2]+tree[node*2+1];

}

void lazy_update(vector<long long>&lazy, vector<long long>&tree , int node , int start , int end)
{
    if (lazy[node]!=0)
    {
        tree[node]+=(end-start+1)*lazy[node];
        if (start!=end)
        {
            lazy[node*2]+=lazy[node];
            lazy[node*2+1]+=lazy[node];
        }

        lazy[node]=0;
    }
}

void tree_update(vector<long long>&lazy, vector<long long>&tree , int node , int start , int end , int left , int right , long long diff)
{
    lazy_update(lazy, tree , node , start , end);

    if (left > end || right < start)
    {
        return ;
    }

    if (left<=start && right>=end)
    {
        tree[node]+=(end-start+1)*diff;

        if (start!=end)
        {
            lazy[node*2]+=diff;
            lazy[node*2+1]+=diff;
        }
        return ;
    }

    tree_update(lazy , tree , node*2 , start , (start+end)/2 , left , right , diff);
    tree_update(lazy , tree , node*2+1,  (start+end)/2+1 , end , left , right , diff);

    tree[node]=tree[node*2]+tree[node*2+1];

}

long long query(vector<long long>&lazy , vector<long long> &tree, int node , int start , int end , int left , int right)
{

    lazy_update(lazy, tree , node , start , end);

    if (left>end || right <start)
    {
        return 0;
    }

    if (left<=start && right>=end)
    {
        return tree[node];
    }

    return query(lazy, tree , node*2 , start  , (start+end)/2 , left , right)+query(lazy , tree,node*2+1,  (start+end)/2+1 , end , left,  right);

}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N , M , K;

    cin >> N >> M >> K;

    vector<long long> L(N);

    vector<long long> tree(4*N);
    vector<long long> lazy(4*N);

    for (int i = 0; i < N ; i ++)
    {
        cin >> L[i];
    
    }

    M+=K; // 쿼리 개수 합치기/

    init(L , tree, 1, 0 , N-1);

    while ( M-- )
    {
        int Q;

        cin >> Q;

        if (Q==1)
        {
            int left, right;
            long long diff;
            cin >> left >> right >> diff;
            tree_update(lazy, tree, 1,  0 , N-1,  left-1 , right-1 , diff);

            
        }
        else
        {
            int left ,right;

            cin >> left >> right;

            cout << query(lazy, tree , 1 , 0, N-1, left-1 , right-1 ) << "\n" ;
        }
    }
}