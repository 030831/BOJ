from collections import deque
import sys
input=sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

graph=[] ; deq=deque()
m,n,h=map(int,input().split())
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                deq.append([i,j,k])
    graph.append(tmp)

while deq:
    x,y,z=deq.popleft()

    for i in range(6):
        a=x+dx[i]
        b=y+dy[i]
        c=z+dz[i]

        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            deq.append([a,b,c])
            graph[a][b][c]=graph[x][y][z]+1

day=0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit()
        day=max(day,max(j))

print(day-1)

