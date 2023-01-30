from collections import deque
import sys
input=sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


a,b=map(int,input().split())
graph=[] ; deq=deque()

for i in range(a):
    graph.append(list(map(int,input().split())))




def BFS(graph,x,y):
    deq.append((x,y))
    graph[x][y]=0
    count=1

    while deq:
        x,y=deq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=a or ny<0 or ny>=b:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                deq.append( (nx,ny) )
                count+=1
    return count

paint=[]

for i in range(a):
    for j in range(b):
        if graph[i][j]==1:
            paint.append(BFS(graph,i,j))


if len(paint)==0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))