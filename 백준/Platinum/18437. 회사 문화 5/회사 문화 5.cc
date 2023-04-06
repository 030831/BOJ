#include <iostream>
#include <bits/stdc++.h>
#include <vector>

#define MAX 100001

using namespace std;

vector<vector<int>> graph(MAX);
vector<int> tree(4*MAX);
vector<int> lazy(4*MAX);

int START[MAX] , END[MAX];


int N,M,K,cnt;

/**
 * 백준 18437 - 회사문화 5
 * 1 i: i번 직원을 상사로 가지고 있는 모든 직원은 컴퓨터를 켠다.
 * 2 i: i번 직원을 상사로 가지고 있는 모든 직원은 컴퓨터를 끈다.
 * 3 i: i번 직원을 상사로 가지고 있는 직원 중에서 컴퓨터가 켜져있는 사람의 수를 출력한다.
 */

void lazy_update(int node , int start , int end )
{
    if (lazy[node]!=-1) {
        tree[node] = (end-start+1)*lazy[node];

        if (start!=end) {
            lazy[node<<1] = lazy[node];
            lazy[node<<1|1] = lazy[node];
        }
        lazy[node] = -1;
    }
}

int init(int node,  int start , int end)
{
    lazy[node]= -1;
    if (start==end) {
        return tree[node]=1;
    }
    return tree[node] = init(node<<1 , start , (start+end)/2 ) + init(node<<1|1 , (start+end)/2+1 , end);
}

void update(int node , int start , int end , int left , int right , int value)
{
    lazy_update(node,  start , end);

    if (left>end || right<start) {
        return;
    }

    if (left<=start && right>=end) {
        lazy[node] = value;
        lazy_update(node,  start , end);
        return;
    }

    update(node<<1 , start , (start+end)/2 , left , right , value);
    update(node<<1|1 , (start+end)/2+1 , end , left , right , value);
    tree[node] = tree[node<<1] + tree[node<<1|1];
}

int query(int node , int start , int end , int left , int right)
{
    lazy_update(node,  start , end);

    if (left>end || right<start) {
        return 0;
    }

    if (left<=start && right>=end) {
        return tree[node];
    }

    return query(node<<1 , start , (start+end)/2 , left , right) + query(node<<1|1 , (start+end)/2+1 , end , left, right);
}


void dfs(int node)
{
    START[node]= ++cnt;

    for (int nextNode : graph[node]) {
        dfs(nextNode);
    }

    END[node] = cnt;
}

int main()
{
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);
    cin >> N;

    for (int i = 1 ; i<=N ; i++) {
        cin >> K;
        if (K!=0) {
            graph[K].push_back(i);
        }
    }
    dfs(1);
    init(1,1,N);

    cin >> M;
    for (int i = 0 ; i < M ; i++) {
        int a,b;
        cin >> a >> b;
        if (a==1) {
            update(1,1,N,START[b]+1, END[b] , 1);
        }
        else if (a==2) {
            update(1,1,N,START[b]+1, END[b] , 0);
        }
        else {
            cout << query(1,1,N,START[b]+1 , END[b]) << '\n';
        }

    }


}
