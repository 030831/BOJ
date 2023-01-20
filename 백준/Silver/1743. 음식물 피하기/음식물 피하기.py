import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**4)

N,M,K=map(int,input().split())
dx=[-1,0,0,1]
dy=[0,-1,1,0]
graph=[ ["."]*M for _ in range(N) ]

for i in range(K):
    a,b=map(int,input().split())
    graph[a-1][b-1]="#"


def DFS(x,y):
    cnt=1
    visit[x][y]=1
    for i in range(4):
        nx=x+dx[i] ; ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny]=="#" and visit[nx][ny]==0:
                visit[nx][ny]=1
                cnt+=DFS(nx,ny)
    return cnt

answer=0
visit = [[0] * (M + 1) for i in range(N + 1)]

for i in range(N):
    for j in range(M):
        if graph[i][j]=="#":
            answer=max(answer,DFS(i,j))
print(answer)
