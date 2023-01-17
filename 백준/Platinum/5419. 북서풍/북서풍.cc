#include <bits/stdc++.h>

using namespace std;
int T, N;
vector<int> L , tree;

void update(int node , int start , int end , int index)
{
    if (index<start || index>end)
    {
        return;
    }

    if (start==end)
    {
        tree[node]++;
        return;
    }

    update(node*2 , start , (start+end)/2 , index);
    update(node*2+1 , (start+end)/2+1 , end , index);

    tree[node]=tree[node*2]+tree[node*2+1];

}

long long query(int node , int start , int end , int left , int right)
{
    if (left>end || right<start)
    {
        return 0;
    }

    if (left<=start && right>=end)
    {
        return tree[node];
    }

    return query(node*2 , start , (start+end)/2 , left ,right) + query(node*2+1 , (start+end)/2+1 , end , left ,right);
}
int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> T;

    while (T--)
    {
        cin >> N;

        vector<int> sorted;
        vector<pair <int,int> > V;
        map<int,int> location;


        L=vector<int> (N,0);
        tree=vector<int> (4*N,0);

        
        for (int i = 0 ; i < N ;  i++)
        {
            int x,y;
            cin >> x >> y;
            V.push_back({-x,y});
            sorted.push_back(y);
        }

        sort(V.begin() , V.end());
        sort(sorted.begin() , sorted.end());

        for (int i = 0 ; i < N ; i++)
        {
            location[sorted[i]]=i; // 좌표압축.
        }
        
        long long answer=0;

        for (auto Index : V)
        {
            answer+=query(1,0,N-1, 0, location[Index.second]);
            update(1,0,N-1,location[Index.second]);
        }

        cout << answer << "\n";
    }

    return 0;
}