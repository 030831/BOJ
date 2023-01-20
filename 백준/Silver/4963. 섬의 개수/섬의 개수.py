import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

dx=[-1,1,0,0 ,1,1,-1,-1]
dy=[0,0,-1,1 ,1,-1,1,-1]


def DFS(i,j):

    visit[i][j]=True

    for node in range(8):
        x=i+dx[node] ; y=j+dy[node]

        if 0<=x<M and 0<=y<N and visit[x][y]==False and graph[x][y]==1:
            DFS(x,y)


while True:

    N,M=map(int,input().split())

    if N==0 and M==0:
        break

    graph=[ list(map(int,input().split())) for _ in range(M) ]

    visit=[ [False]*N for _ in range(M) ]

    total=0
    for i in range(M):
        for j in range(N):
            if visit[i][j]==False and graph[i][j]==1:
                total+=1
                DFS(i,j)

    print(total)