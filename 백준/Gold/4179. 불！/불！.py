import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS():

    while deq_f:
        x,y=deq_f.popleft()

        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if not visit_f[nx][ny] and graph[nx][ny]!="#":
                    visit_f[nx][ny]=visit_f[x][y]+1
                    deq_f.append((nx,ny))
    while deq_j:
        x,y=deq_j.popleft()

        for i in range(4):
            nx= x +dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]!="#" and not  visit_j[nx][ny]:
                    if not visit_f[nx][ny] or visit_f[nx][ny]>visit_j[x][y]+1:
                        visit_j[nx][ny]=visit_j[x][y]+1
                        deq_j.append((nx,ny))
            else:
                return visit_j[x][y]
    return "IMPOSSIBLE"


N,M=map(int,input().split())

graph=[ list(input().rstrip()) for _ in range(N) ]

deq_j=deque() ; deq_f=deque()
visit_j=[ [0]*M for _ in range(N) ]
visit_f=[ [0]*M for _ in range(N) ]

for i in range(N):
    for j in range(M):
        if graph[i][j]=="J":
            deq_j.append((i,j))
            visit_j[i][j]=1
        elif graph[i][j]=="F":
            deq_f.append((i,j))
            visit_f[i][j]=1

print( BFS() )