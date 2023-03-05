import sys
input=sys.stdin.readline
from collections import deque
from itertools import combinations

LMI=lambda:list(map(int,input().split()))
MI=lambda:map(int,input().split())
G=lambda x:[ LMI() for _ in range(x) ]
V=lambda x,y:[ [False]*y for _ in range(x) ]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(select):
    copy_graph=[ i[:] for i in select_graph]
    Q=deque()
    for x,y in select:
        copy_graph[x][y]=2
        Q.append([x,y])

    visit=[ [0]*N for _ in range(N) ]
    while Q:
        x,y=Q.popleft()

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<N and 0<=ny<N and copy_graph[nx][ny]!=2 and not visit[nx][ny]:
                visit[nx][ny]=visit[x][y]+1
                Q.append([nx,ny])

    total = 0
    for x,y in check:
        total+=visit[x][y]
    return total

N,M=MI()
graph=G(N)

chicken=[] ; Q=deque() ; check=[]

select_graph=[ [0]*N for _ in range(N) ]
for i in range(N):
    for j in range(N):
        if graph[i][j]==2:
            chicken.append((i,j))
        elif graph[i][j]==1:
            check.append([i,j])
            select_graph[i][j]=1


ans=int(1e9)
for i in combinations(chicken , M):
    ans=min(ans,BFS(i))

print(ans)

