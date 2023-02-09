import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS():

    global time
    deq2=deque()
    a,b=0,0
    while deq:
        x,y=deq.popleft()

        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
                if not graph[nx][ny]:
                    deq.append((nx, ny))
                else:
                    deq2.append((nx,ny))
                visit[nx][ny]=True

        if len(deq)==0:
            if len(deq2):
                a = time
                b = len(deq2)
            for x,y in deq2:
                graph[x][y]=time
                deq.append((x,y))
            deq2.clear()
            time+=1

    print(a,b,sep='\n')




N,M=map(int,input().split())
graph=[ list(map(int,input().split())) for _ in range(N) ]
deq=deque() ; deq.append((0,0))
visit = [[False] * M for _ in range(N)]
time = 1 ; count = 0
BFS()
