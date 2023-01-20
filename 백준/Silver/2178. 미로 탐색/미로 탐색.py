from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def BFS():

    deq=deque()
    deq.append([0,0])

    while deq:

        x,y=deq.popleft()

        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                deq.append([nx,ny])

    return graph[N-1][M-1]

N,M=map(int,input().split())

graph=[ list(map(str,input().rstrip())) for _ in range(N) ]

for i in range(N):
    for j in range(M):
        graph[i][j]=int(graph[i][j])


print( BFS() )

