import sys
input=sys.stdin.readline
from collections import deque
LMI=lambda:list(map(int,input().split()))
LMS=lambda:list(map(str,input().split()))
MI=lambda:map(int,input().split())
I=lambda:int(input())
GI=lambda x:[ LMI() for _ in range(x) ]
GS=lambda x:[ LMS() for _ in range(x) ]
V=lambda x,y:[ [False]*y for _ in range(x) ]

dx=[-1,1,0,0]
dy=[0,0,-1,1] # 위 아래 왼쪽 오른쪽.

def view(ViewGraph):
    for i in ViewGraph:
        print(i)
    print()

def setGraph(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                graph[i][j]='#'

def findPeople(graph,x,y):
    global visit_people
    P=[] ; visit=[ [0]*N for _ in range(N) ] ; visit[x][y]=1
    Q=deque() ; Q.append((x,y))

    if graph[x][y]: # 시작위치에 이미 값이 있을경우
        P.append((x,y,graph[x][y],1))
    while Q:
        x,y=Q.popleft()

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<N and 0<=ny<N and not visit[nx][ny] and graph[nx][ny]!='#':
                visit[nx][ny] = visit[x][y] + 1
                Q.append((nx, ny))
                if graph[nx][ny]!=0:
                    P.append((nx,ny,graph[nx][ny],visit[nx][ny]))
    if P:
        P.sort(key=lambda x: (x[3], x[0], x[1],x[2]))
        for nx,ny,graphValue,visitValue in P:
            if not visit_people[graphValue]:
                visit_people[graphValue]=True
                return nx,ny,graphValue,visitValue
        return -1,-1,-1,-1
    else:
        return -1,-1,-1,-1

def goToWant(graph,start_x,start_y,want_x,want_y):
    visit = [[0] * N for _ in range(N)] ; visit[start_x][start_y] = 1
    Q = deque() ; Q.append((start_x, start_y))

    while Q:
        x,y=Q.popleft()

        if [x,y]==[want_x,want_y]:
            return visit[x][y]

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<N and 0<=ny<N and not visit[nx][ny] and graph[nx][ny]!='#':
                Q.append((nx,ny))
                visit[nx][ny]=visit[x][y]+1
    return -1
def bfs():
    global start_x,start_y,K,graph,people

    start_x,start_y,want,value = findPeople(graph,start_x,start_y)
    K -= (value - 1)
    if [start_x,start_y,want,value] == [-1,-1,-1,-1]:
        return False
    if K<=0:
        return False

    value = goToWant(graph,start_x,start_y,people[want][0],people[want][1])

    if value==-1:
        return False
    K -= (value - 1)

    if K < 0: # 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
        return False

    K+=(value-1)*2

    #택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다.
    start_x,start_y=people[want][0],people[want][1]
    return True


N,M,K=MI()
graph=GI(N)
setGraph(graph)

start_x,start_y=MI() ; start_x-=1 ; start_y-=1
people=[ [] for _ in range(M+1) ]
visit_people=[False]*(M+1)
for i in range(M):
    a,b,c,d=MI()
    people[i+1].append(c-1)
    people[i+1].append(d-1)
    graph[a-1][b-1] = i+1

ans = 1
for i in range(M):
    ans = bfs()
    if not ans:
        break
if not ans:
    print(-1)
else:
    print(K)
