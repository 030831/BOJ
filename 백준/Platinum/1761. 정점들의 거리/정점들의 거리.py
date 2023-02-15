import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 21

def DFS(node , parent_node , value):
    Depth[node] = Depth[parent_node]+1
    visit[node] = True
    if node!=1:
        dp[node] = dp[parent_node]+value
    for next_node ,cost in graph[node]:
        if not visit[next_node]:
            Parent[next_node][0] = node
            DFS(next_node , node , cost)

def Set_Parent():
    DFS(1,0,0)
    for i in range(1,LOG):
        for j in range(1,N+1):
            Parent[j][i] = Parent[Parent[j][i-1]][i-1]

def LCA(a,b):

    if Depth[a]>Depth[b]:
        a,b=b,a

    for i in range(LOG-1,-1,-1):
        if Depth[b]-Depth[a]>= (1<<i):
            b=Parent[b][i]

    if a==b:
        return a

    for i in range(LOG-1,-1,-1):
        if Parent[a][i]!=Parent[b][i]:
            a=Parent[a][i]
            b=Parent[b][i]

    return Parent[a][0]

N=int(input())

graph=[ [] for _ in range(N+1) ]
Parent=[ [0]*LOG for _ in range(N+1) ]
Depth=[0]*(N+1) ; visit=[0]*(N+1) ; dp=[0]*(N+1)
Depth[0] = -1

for i in range(N-1):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

Set_Parent()

for i in range(int(input())):
    a,b=map(int,input().split())
    print(dp[a]+dp[b]-2*dp[LCA(a,b)])
