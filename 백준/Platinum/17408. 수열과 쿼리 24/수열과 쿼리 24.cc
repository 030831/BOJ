#include <bits/stdc++.h>

using namespace std;
using ll = long long;
pair<int, int> tree[400001];


pair<int , int> merge(pair<int,int> a , pair<int,int>b)
{
    if (a<b)
    {
        swap(a,b); // 더 큰쪽으로 내림차순 정렬
    }

    if (a.second<b.first)
    {
        a.second=b.first; // 더 큰값으로 바꾼다.
    }


    return a;
}

void update(int node , int start , int end , int index , int value)
{
    if (index<start || index>end)
    {
        return;
    }

    if (start==end)
    {
        tree[node]={value , -1e9};
        return;
    }

    update(node*2 , start , (start+end)/2 , index , value);
    update(node*2+1 , (start+end)/2+1 , end , index , value);

    tree[node]= merge(tree[node*2] , tree[node*2+1]); 
    // 트리의 부모는 자식의 값 4개중 최대값 2개를 가져간다.
}

pair<int,int> query(int node , int start , int end ,  int left , int right )
{
    if (left>end || right<start)
    {
        return {-1e9 , -1e9};
    }
    if (left<=start && right>=end)
    {
        return tree[node];
    }

    return merge( query(node*2 , start , (start+end)/2 ,left, right) , query(node*2+1 ,(start+end)/2+1 , end , left ,right));
}

int total(pair<int,int> a)
{
    return a.first+a.second;
}

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;

    for (int i = 1 ; i <=N ; i++)
    {
        int value;
        cin >> value;
        update(1,1,N, i,  value);
    }

    int M;
    cin >> M;

    while (M--)
    {
        int a,b,c;
        cin >> a >> b >> c;

        if (a==1)
        {
            update(1,1,N,b,c);
        }
        else
        {
            cout << total(query(1,1,N,b,c)) << "\n";
        }
    }

}
