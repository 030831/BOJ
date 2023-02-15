import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
LOG = 21

def DFS(node , deep):
    visit[node] =True
    Depth[node] = deep

    for i in graph[node]:
        if not visit[i]:
            Parent[i][0]=node
            DFS(i , deep+1)

def Set_Parent():
    DFS(1,0) # 루트노드는 1번노드
    for i in range(1,LOG):
        for j in range(1,N+1):
            Parent[j][i] = Parent[Parent[j][i-1]][i-1]
            # 부모노드에 자식노드의 값을 2^N 에 비례하여 저장한다.

def LCA(a,b):

    if Depth[a]>Depth[b]:
        a,b=b,a

    for i in range(LOG-1 , -1 , -1):
        if Depth[b]-Depth[a]>=(1<<i):
            # 깊이가 동일하게 맞출때 2^N 만큼 이동해준다.
            b=Parent[b][i]

    if a==b:
        return a

    for i in range(LOG-1,-1,-1):
        if Parent[a][i]!=Parent[b][i]: # 두 부모가 다르다면
            a=Parent[a][i]
            b=Parent[b][i]
    return Parent[a][0]



N=int(input())

Parent=[ [0]*LOG for _ in range(N+1) ]
Depth = [0]*(N+1)
visit=[False]*(N+1)
graph=[ [] for _ in range(N+1) ]

for i in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

Set_Parent()

M=int(input())

for i in range(M):
    a,b=map(int,input().split())
    print(LCA(a,b))