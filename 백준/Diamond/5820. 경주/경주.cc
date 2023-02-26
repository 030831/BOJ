#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 200001;
const int MAX_K = 1000001;
const int INF = 1e9;

int N,K;
int u,v,w;
int Answer;
int sized[MAX_N],visited[MAX_N],check[MAX_N];
vector<pair<int,int>> graph[MAX_N];
vector<int> tree;

// i.first = next_node , i.second = weight
int get_size(int node , int pre);
int get_Centroid(int node , int pre , int sub_tree_size ) ;
int Find_Min_Dis(int node , int pre , int dis , int deep);
void update(int node , int pre , int dis , int deep);
int Centroid_Decomposition(int node); // 센트로이드 분할.
void input();

int get_size(int node , int pre) // 트리의 크기를 구하는 함수, 파라미터는 현재노드와 이전노드를 사용한다.
{
    sized[node] = 1 ; // 트리의 크기를 저장할 배열 , 초기값은 1로 저장한다.
    for ( auto i : graph[node])
    {
        if (i.first == pre || visited[i.first]) // 다음이동할 노드가 이전의 노드와 같거나 방문한 지점이라면
        {
            continue;
        }
        sized[node] += get_size(i.first, node); // 트리의 크기를 저장할 배열에 재귀탐색으로 다음노드와 현재노드를 파라미터값으로 넣는다.
    }
    return sized[node]; //트리의 크기를 반환한다.
}
int get_Centroid(int node , int pre , int sub_tree_size ) // 센트로이드의 크기를 구하는 함수
{
    for ( auto i : graph[node])
    {
        if (i.first == pre || visited[i.first])
        {
            continue;
        }
        if (sized[i.first] > sub_tree_size) 
        {
            return get_Centroid(i.first, node , sub_tree_size);
        }
    }
    
    return node;
}
int Find_Min_Dis(int node , int pre , int dis , int deep)
{
    int ret = INF;
    if (dis > K)  // 거리가 찾고자 하는 K 보다 크다면
    {
        return ret;
    }

    ret = min(ret , check[K-dis]+deep); 
    // 다른 서브트리에서 K-x 만큼 떨어진 정점이 있다면 현재정점의 깊이 + K-x인 정점의 최소깊이로 갱신.

    for (auto i : graph[node])
    {
        if (i.first == pre || visited[i.first])
        {
            continue;
        }

        ret = min(ret , Find_Min_Dis(i.first , node , dis+i.second , deep+1));
        // 재귀탐색으로 트리를 탐색한다.
    }

    return ret;
}

void update(int node , int pre , int dis , int deep)
{
    if (dis > K)
    {
        return;
    }

    check[dis] = min(check[dis] , deep); // check 배열에 트리의 깊이를 저장한다.
    tree.push_back(dis);

    for (auto i : graph[node])
    {
        if (i.first == pre || visited[i.first])
        {
            continue;
        }
        update(i.first , node , dis+i.second , deep+1);
    }
}

int Centroid_Decomposition(int node) // 센트로이드 분할.
{
    int tree_size = get_size(node , -1); // 트리의 크기를 저장한다.
    int centroid_size = get_Centroid(node , -1,  tree_size/2);   //센트로이드의 정점을 구한다.
    int ret = INF; // 경로의 최소값을 저장할 변수

    for (auto i : tree)
    {
        check[i] = INF; // update 를 통해 방문한 지점은 INF 로 초기화한다.
    }

    tree.clear();
    visited[centroid_size]=1; // 방문처리
    check[0]=0; 

    for ( auto i : graph[centroid_size])
    {
        if (visited[i.first])
        {
            continue;
        }
        ret = min(ret , Find_Min_Dis(i.first, centroid_size , i.second , 1)); 
        update(i.first ,centroid_size , i.second , 1);
    }

    for (auto i : graph[centroid_size])
    {
        if (visited[i.first])
        {
            continue;
        }
        ret = min(ret ,Centroid_Decomposition(i.first) );
    }

    return ret;
}
void input()
{
    cin >> N >> K;
    for (int i = 1 ; i < N ; i++)
    {
        cin >> u >> v >> w;
        graph[u].push_back(make_pair(v,w));
        graph[v].push_back(make_pair(u,w));
    }

    fill(check,  check+K+1 , INF);

}
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    input();

    Answer = Centroid_Decomposition(0); 

    if (Answer == INF) // 경로가없다면 -1 출력
    {
        cout << -1;
    }
    else
    {
        cout << Answer;

    }
}