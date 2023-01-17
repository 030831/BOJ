from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,0,0,1]
dy=[0,-1,1,0]
high,breath=map(int,input().split())
graph=[]

for i in range(high):
    graph.append(list(input()))


def BFS(x,y):
    global count
    deq=deque()
    deq.append([x,y])
    visit[x][y]=1
    
    while deq:
        x,y=deq.popleft()
        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]
            if 0<=nx<high and 0<=ny<breath and graph[nx][ny]=='L':
                if visit[nx][ny]==0:
                    visit[nx][ny]=visit[x][y]+1
                    count=max(count,visit[x][y]+1)
                    deq.append([nx,ny])
    return count
    
answer=0
for i in range(high):
    for j in range(breath):
        count=0
        visit=[ [0]*breath for i in range(high) ]
        if graph[i][j]=='L':
            answer=max(answer,BFS(i,j))

print(answer-1)