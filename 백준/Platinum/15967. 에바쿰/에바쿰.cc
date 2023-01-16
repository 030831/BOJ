#include <iostream>
#include <vector>

using namespace std;

void init(vector<int> &L , vector<int> &tree , int node , int start , int end )
{

    if (start==end)
    {
        tree[node]=L[start];
        return;
    }

    init(L , tree , node*2,  start , (start+end)/2);
    init(L , tree , node*2+1 , (start+end)/2+1 , end);

    tree[node]=tree[node*2]+tree[node*2+1];
}

void lazy_update(vector<int>&lazy , vector<int>&tree , int node , int start , int end)
{

    if (lazy[node]!=0)
    {
        tree[node]+=lazy[node]*(end-start+1);

        if (start!=end)
        {
            lazy[node*2]+=lazy[node];
            lazy[node*2+1]+=lazy[node];
        }
        lazy[node]=0;
    }
}

void tree_update(vector<int>&lazy , vector<int>&tree , int node , int start , int end , int left , int right , int diff)
{
    lazy_update(lazy,tree,node,start,end);

    if (left>end || right<start)
    {
        return;
    }

    if (left<=start && right>=end)
    {
        tree[node]+=diff*(end-start+1);
        
        if (start!=end)
        {
            lazy[node*2]+=diff;
            lazy[node*2+1]+=diff;
        }
    }

    tree_update(lazy,tree,node*2, start , (start+end)/2 , left , right , diff);
    tree_update(lazy, tree , node*2+1 , (start+end)/2+1 , end , left , right , diff);

    tree[node]=tree[node*2]+tree[node*2+1];
}

long long query(vector<int>&lazy , vector<int>&tree , int node , int start , int end , int left , int right)
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

    return query(lazy,tree, node*2 , start  , (start+end)/2 , left , right) + query(lazy , tree , node*2+1 , (start+end)/2+1 , end , left ,right);


}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N,Q1,Q2;

    cin >> N >> Q1 >> Q2;

    vector<int> tree(4*N);
    vector<int> lazy(4*N);
    vector<int> L(N);

    for (int i = 0 ; i < N ; i ++)
    {
        cin >> L[i];
    }

    init(L,tree,1,0,N-1);

    Q1+=Q2;

    while (Q1--)
    {

        int q;

        cin >> q;
        if (q==1)
        {
            int a, b;
            cin >> a >> b;

            cout << query(lazy,tree,1,0,N-1,a-1,b-1) << "\n";
        }
        else
        {
            int s,e,l;

            cin >> s >> e >> l;

            tree_update(lazy,tree,1,0,N-1,s-1 , e-1 , l);
        }
    }
}