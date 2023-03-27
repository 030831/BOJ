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

def view(ViewGraph):
    for i in ViewGraph:
        print(i)
    print()


left = [ (-2,0,2) , (2,0,2) , (-1,0,7) , (1,0,7) , (-1,-1,10) , (1,-1,10) , (-1,1,1) , (1,1,1) , (0,-2,5) ,(0,-1,-1) ]
right= [ (-2,0,2) , (2,0,2) , (-1,0,7) , (1,0,7) , (-1,-1,1) , (1,-1,1) , (-1,1,10) , (1,1,10) , (0,2,5) ,(0,1,-1) ]
up = [ (-2,0,5) , (-1,0,-1) , (-1,-1,10) , (-1,1,10) , (0,-1,7) , (0,1,7) , (1,-1,1) , (1,1,1) , (0,-2,2) , (0,2,2) ]
down = [ (2,0,5) , (1,0,-1) , (1,-1,10) , (1,1,10) , (-1,-1,1) , (-1,1,1) , (0,-2,2) , (0,2,2) , (0,-1,7) , (0,1,7) ]

D=[ left , down , right , up ]
dx=[0,1,0,-1]
dy=[-1,0,1,0]


def spread():
    global ans

    startValue,ax,ay=0,-1,-1
    for i in range(len(D[direction])):
        nx,ny,rate=x+D[direction][i][0], y+D[direction][i][1] , D[direction][i][2]

        if 0<=nx<N and 0<=ny<N and rate>0:
            graph[nx][ny]+=int(graph[x][y]*(rate/100))
            startValue+=int(graph[x][y]*(rate/100))
        elif 0<=nx<N and 0<=ny<N and rate==-1:
            ax,ay=nx,ny
        else:
            if rate!=-1:
                ans+=int(graph[x][y]*(rate/100))
                startValue += int(graph[x][y] * (rate / 100))

    if [ax,ay]!=[-1,-1]:
        graph[ax][ay]+=graph[x][y]-startValue
    else:
        ans+=graph[x][y]-startValue
    graph[x][y] = 0


# 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.
# 토네이도는 한 번에 한 칸 이동한다.
# y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다.
def move():
    global x,y,S,direction,moveCount

    for i in range(S):

        if 0<=x+dx[direction]<N and 0<=y+dy[direction]<N:
            now = graph[x][y] ; graph[x][y]=0
            x+=dx[direction] ; y+=dy[direction]
            graph[x][y] += now
            spread()

    moveCount+=1
    direction+=1

    if moveCount%2==0: # 2번이동했다면
        S+=1
    if direction%4==0:
        direction=0



N=I()
graph=GI(N)
x,y=N//2,N//2 ; S = 1 ; moveCount = 0 ; direction = 0
ans = 0

while True:
    if x==0 and y==0:
        break
    move()

print(ans)