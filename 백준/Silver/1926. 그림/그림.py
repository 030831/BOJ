from collections import deque
import sys
input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(x,y):
    deq=deque()
    deq.append([x,y])
    visit[x][y]=1
    check=1
    while deq:
        x,y=deq.popleft()
        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and graph[nx][ny]==1:
                visit[nx][ny]=1
                check+=1
                deq.append([nx,ny])

    return check  # check 라는 변수는 총 이동횟수

N,M=map(int,input().split())

graph=[ list(map(int,input().split())) for _ in range(N) ]
visit=[ [0]*M for _ in range(N) ]

count=0 ; tmp=0 # count = 종이의 개수 , tmp = 종이의 넓이.

for i in range(N):
    for j in range(M):
        if graph[i][j]==1 and not visit[i][j]: # 그래프의 값이 1 이고 방문하지 않은 지점이라면
            tmp=max(tmp , BFS(i,j) ) # 방문을 해주고 , 그때의 종이의 넓이의 최대값을 갱신한다.
            count+=1 # 종이의 개수.

print(count , tmp , sep='\n')