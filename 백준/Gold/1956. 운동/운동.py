import sys
input=sys.stdin.readline

INF = int(1e9)

def Floyd_Warshall():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j]=min(graph[i][j] , graph[i][k]+graph[k][j])

N,M=map(int,input().split())

graph=[ [INF]*(N+1) for _ in range(N+1) ]

for i in range(M):
    start,end,cost=map(int,input().split())
    graph[start][end]=cost




Floyd_Warshall()

Answer=INF

for i in range(1,N+1):
    Answer=min(Answer, graph[i][i])

if Answer==INF:
    print(-1)
else:
    print(Answer)