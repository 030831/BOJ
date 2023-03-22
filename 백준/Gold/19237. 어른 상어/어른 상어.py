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

def setSharkLocation():
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                shark[graph[i][j]]=[i,j]

def setSharkPriorityDirection():

    for i in range(M):
        for j in range(4):
            sharkPriorityDirection[i].append(LMI())

def setShark():
# 각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.
    for i in range(1, M + 1):
        shark[i]=[*shark[i],L[i-1]]

def setSmell():
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                smell[i][j]= [K,graph[i][j]]

def goTomove(shark, number,x,y,direction , visit , delete ,  nextSmell):
#상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.
#먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
#자신의 냄새가 있는 칸이 여러가지일 수 도 있다.

    for i in sharkPriorityDirection[number-1][direction-1]:
        nx,ny=x+dx[i-1],y+dy[i-1]
        if 0<=nx<N and 0<=ny<N and not smell[nx][ny][0]: # 빈칸먼저탐색
            if not visit[nx][ny]:
                visit[nx][ny]=number
                shark[number] = [nx,ny,i]
                nextSmell.append((nx,ny,number))
                return
            if number>visit[nx][ny]:
                delete.append(number)
                return
            if number<visit[nx][ny]:
                delete.append(visit[nx][ny])
                visit[nx][ny]=number
                shark[number] = [nx,ny,i]
                nextSmell.append((nx, ny,number))
                return
            if number==visit[nx][ny]:
                shark[number] = [nx,ny,i]
                nextSmell.append((nx,ny,number))
                return

    for i in sharkPriorityDirection[number-1][direction-1]: # 빈칸이 없으면 이전에 이동했던 칸들중 탐색
        nx,ny=x+dx[i-1],y+dy[i-1]
        if 0<=nx<N and 0<=ny<N and smell[nx][ny][1] == number:
            if not visit[nx][ny]:
                visit[nx][ny]=number
                shark[number] = [nx,ny,i]
                nextSmell.append((nx,ny,number))
                return
            if number>visit[nx][ny]:
                delete.append(number)
                return
            if number<visit[nx][ny]:
                delete.append(visit[nx][ny])
                visit[nx][ny]=number
                shark[number] = [nx,ny,i]
                nextSmell.append((nx, ny,number))
                return
            if number==visit[nx][ny]:
                shark[number] = [nx,ny,i]
                nextSmell.append((nx,ny,number))
                return


def decreaseSmell(nextSmell):

    for i in range(N):
        for j in range(N):
            if smell[i][j][0]:
                smell[i][j][0]-=1

    for x,y,number in nextSmell:
        smell[x][y] = [K , number]

    for i in range(N):
        for j in range(N):
            if not smell[i][j][0] and smell[i][j][1]:
                smell[i][j][1] = 0
def move():
    visit=[ [0]*N for _ in range(N) ]
    delete=[] ; nextSmell=[]

    for number,i in shark.items():
        x,y,direction = i
        goTomove(shark,number,x,y,direction , visit , delete , nextSmell)
        #먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.

    for number in delete:
        del shark[number]

    decreaseSmell(nextSmell)

N,M,K=MI()
graph=GI(N)

shark=dict()
# 상어의 좌표와 방향이 필요함.

sharkPriorityDirection=[ [] for _ in range(M) ]
smell = [ [[0,0]]*N for _ in range(N) ]
L=LMI()

setSmell()
setSharkLocation()
setShark()
setSharkPriorityDirection()

ans = 1001
for i in range(1,1001):
    move()
    if len(shark)==1:
        ans = i
        break
if ans==1001:
    print(-1)
else:
    print(ans)
