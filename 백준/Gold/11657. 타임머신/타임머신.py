import sys
input=sys.stdin.readline
INF=float('inf')

def Bellman_Ford(start):
    dp[start]=0

    for i in range(N):
        for j in range(M):
            node = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]

            if dp[node]!=INF and dp[node]+cost < dp[next_node]:
                dp[next_node]=dp[node]+cost

                if i==N-1:
                    return True
    return False



N,M=map(int,input().split())
graph=[] ; dp=[INF]*(N+1)
for i in range(M):
    a,b,c=map(int,input().split())
    graph.append((a,b,c))


Answer = Bellman_Ford(1)

if Answer:
    print(-1)
else:
    for i in range(2,N+1):
        if dp[i]==INF:
            print(-1)
        else:
            print(dp[i])