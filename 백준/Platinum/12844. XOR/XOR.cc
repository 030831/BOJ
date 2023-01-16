#include <iostream>
#include <vector>

using namespace std;

void init(vector<long long>&L , vector<long long>&tree , int node , int start , int end)
{
    if (start==end)
    {
        tree[node]=L[start];
        return;
    }

    init(L , tree, node*2 , start , (start+end)/2);
    init(L , tree , node*2+1 , (start+end)/2+1 , end);

    tree[node]=tree[node*2]^tree[node*2+1];

}

void lazy_update(vector<long long>&lazy , vector<long long>&tree , int node , int start , int end)
{
    if (lazy[node]!=0)
    {
        tree[node]^=lazy[node]* ((end-start+1)%2);

        if (start!=end)
        {
            lazy[node*2]^=lazy[node];
            lazy[node*2+1]^=lazy[node];
        }

        lazy[node]=0;
    }
}

long long tree_update(vector<long long>&lazy , vector<long long>&tree , int node , int start , int end , int left , int right , int diff)
{

    lazy_update(lazy , tree , node, start ,end);

    if (left>end || right<start)
    {
        return tree[node];
    }

    if (left<=start && right>=end)
    {
        tree[node]^=diff * ((end-start+1)%2);

        if (start!=end)
        {
            lazy[node*2]^=diff;
            lazy[node*2+1]^=diff;
        }
        return tree[node];
    }

    return tree[node]= tree_update(lazy , tree ,node*2 , start ,(start+end)/2 , left ,right , diff) ^ tree_update(lazy , tree , node*2+1 , (start+end)/2+1 , end , left , right , diff);
    // 모든 수를 XOR 해야하므로 전부다 return 을 해서 xor 시킨다.

}

long long query(vector<long long>&lazy , vector<long long>&tree , int node , int start , int end , int left , int right)
{
    lazy_update(lazy , tree , node, start ,end);

    if (left>end || right<start)
    {
        return 0;
    }

    if (left<=start && right>=end)
    {
        return tree[node];
    }

    return query(lazy , tree , node*2 , start , (start+end)/2 , left , right)^query(lazy , tree , node*2+1 , (start+end)/2+1 , end , left , right);

}
int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;

    cin >> N;

    vector<long long> tree(4*N);
    vector<long long> lazy(4*N);
    vector<long long> L(N);
    
    for (int i = 0 ; i < N ; i ++)
    {
        cin >> L[i];
    }

    init(L , tree , 1,  0 , N-1);


    int M;

    cin >> M;

    while (M--)
    {
        int Q;

        cin >> Q;

        if (Q==1)
        {
            int left, right , K;

            cin >> left >> right >> K;

            tree_update(lazy ,tree , 1 , 0 , N-1 , left , right , K);
        }
        else
        {
            int left_index , right_index;

            cin >> left_index >> right_index;

            cout << query(lazy , tree , 1 , 0 , N-1 , left_index , right_index) << "\n";

        }
    }

}