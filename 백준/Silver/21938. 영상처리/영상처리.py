from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(x,y):
    deq=deque()
    deq.append([x,y])
    visit[x][y]=True

    while deq:
        x,y=deq.popleft()

        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1 and not visit[nx][ny]:
                visit[nx][ny]=True
                deq.append([nx,ny])

N,M=map(int,input().split())

graph=[ [0]*M for _ in range(N) ]

for i in range(N):
    L=list(map(int,input().split()))
    total = 0 ; count = 0 ; index = 0
    for j in range(len(L)):
        total+=L[j]
        count+=1
        if count==3:
            graph[i][index]=total//3
            index+=1 ; count=0 ; total=0

T=int(input())

for i in range(N):
    for j in range(M):
        if graph[i][j]>=T:
            graph[i][j]=1
        else:
            graph[i][j]=0


visit=[ [False]*M for _ in range(N) ]
tmp=0


for i in range(N):
    for j in range(M):
        if not visit[i][j] and graph[i][j]==1:
            tmp+=1
            BFS(i,j)

print(tmp)