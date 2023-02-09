import sys
input=sys.stdin.readline

INF = int(1e9)

def Floyd_Warshall():

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j]=min(graph[i][j] , graph[i][k]+graph[k][j]-1)

    total = 0
    for i in range(1,N+1):
        check=0
        for j in range(1,N+1):
            if graph[i][j]==1 or graph[j][i]==1:
                check+=1
        if check==N-1:
            total+=1
    return total



N,M=map(int,input().split())

graph=[ [INF]*(N+1) for _ in range(N+1) ]

for i in range(M):
    a,b=map(int,input().split())
    graph[a][b]=1


print( Floyd_Warshall() )

