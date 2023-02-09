import sys
input=sys.stdin.readline

def Flody_Warshcall():

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k]+graph[k][j]==2:
                    graph[i][j]=1


N=int(input())
graph=[ list(map(int,input().split())) for _ in range(N) ]


Flody_Warshcall()

for i in graph:
    print(*i)