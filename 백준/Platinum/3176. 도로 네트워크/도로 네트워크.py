import sys,math
input=sys.stdin.readline
from collections import deque

N=int(input())
K=int(math.log2(N))+1

graph=[ [] for _ in range(N+1) ]

for i in range(N-1):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

deq=deque([(1,1)])
Depth=[0]*(N+1) ; Depth[1]=1

dp=[ [ [0,0,0] for _ in range(K)] for _ in range(N+1) ]

while deq:
    node , deep = deq.popleft()
    for next_node , cost in graph[node]:
        if not Depth[next_node]:
            deq.append((next_node , deep+1))
            Depth[next_node] = deep+1
            dp[next_node][0] = [node,cost ,cost]


for j in range(1, K):
    for i in range(1, N + 1):
        dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
        dp[i][j][1] = min(dp[i][j-1][1], dp[dp[i][j-1][0]][j-1][1])
        dp[i][j][2] = max(dp[i][j-1][2], dp[dp[i][j-1][0]][j-1][2])

for i in range(int(input())):
    a,b=map(int,input().split())

    Max_cost = 0
    Min_cost = float('inf')

    if Depth[a]>Depth[b]:
        a,b=b,a

    for i in range(K-1,-1,-1):
        if Depth[b]-Depth[a]>= (1<<i):
            Max_cost = max(Max_cost , dp[b][i][2])
            Min_cost = min(Min_cost , dp[b][i][1])
            b=dp[b][i][0]

    if a==b:
        print(Min_cost , Max_cost)
        continue

    for i in range(K-1,-1,-1):
        if dp[a][i][0]!=dp[b][i][0]:
            Max_cost = max(Max_cost , dp[b][i][2] , dp[a][i][2])
            Min_cost = min(Min_cost , dp[b][i][1] , dp[a][i][1])
            a=dp[a][i][0]
            b=dp[b][i][0]

    Max_cost = max(Max_cost , dp[b][0][2] , dp[a][0][2])
    Min_cost = min(Min_cost , dp[b][0][1] , dp[a][0][1])
    print(Min_cost , Max_cost)