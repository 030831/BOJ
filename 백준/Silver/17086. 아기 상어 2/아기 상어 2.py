"""
BFS 를 할때 , 꼭 시작지점이 하나이어야만 하는가?
- 모든 시작지점을 한번에 덱에 넣고 BFS 를 돌리면은 모든 시작점에서의 거리를 구할 수 있다.
5 4
[3, 2, 1, 2]
[2, 2, 2, 2]
[1, 2, 3, 3]
[2, 2, 2, 2]
[3, 3, 2, 1]

5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
"""
import sys
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

def BFS():

    while deq:

        x,y=deq.popleft()
        for i in range(8):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and graph[nx][ny]==0:
                visit[nx][ny]=visit[x][y]+1
                deq.append([nx,ny])

N,M=map(int,input().split())
graph=[ list(map(int,input().split())) for _ in range(N) ]
visit=[ [0]*M for _ in range(N) ]

deq=deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            deq.append([i,j])
            visit[i][j]=1

BFS() # BFS 함수 실행

answer=0
for i in range(N):
    for j in range(M):
        answer=max(answer,visit[i][j]-1)

print(answer)