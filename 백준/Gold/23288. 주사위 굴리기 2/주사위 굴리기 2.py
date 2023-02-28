import sys
input=sys.stdin.readline
from collections import deque

L_I=lambda:list(map(int,input().split()))
I_S=lambda:map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
"""
Move 1 : 동 , 2: 서  , 3:남 , 4:북
"""

def BFS(x,y):

    Q=deque()
    Q.append([x,y])
    visit=[ [False]*M for _ in range(N) ]
    visit[x][y] = True
    check = graph[x][y] ;  count = 1

    while Q:
        x,y=Q.popleft()

        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and graph[nx][ny]==check:
                visit[nx][ny]=True
                Q.append([nx,ny])
                count+=1

    return count*check

def Dice():

    global N,M,K
    breath=deque([4,1,3])
    high=deque([2,1,5,6])
    Move = 1 ; x,y=[0,0]
    total = 0

    while K:
        if Move==1:
            if y==M-1: # 반대 방향
                Move=2
                y-=1
                breath[0], high[1], breath[2], high[3] = high[1], breath[2], high[3], breath[0]
            else:
                y+=1
                breath[0], high[3], breath[2], high[1] = high[3], breath[2], high[1], breath[0]

        elif Move==2:
            if y==0:
                Move=1
                y+=1
                breath[0], high[3], breath[2], high[1] = high[3], breath[2], high[1], breath[0]
            else:
                y-=1
                breath[0], high[1], breath[2], high[3] = high[1], breath[2], high[3], breath[0]
        elif Move==3:
            if x==N-1:
                Move=4
                x-=1
                high.append(high.popleft())
                breath[1] = high[3]
            else:
                x += 1
                high.appendleft(high.pop())
                breath[1] = high[3]
        else:
            if x==0:
                x+=1
                Move=3
                high.appendleft(high.pop())
                breath[1] = high[3]
            else:
                x -= 1
                high.append(high.popleft())
                breath[1] = high[3]

        if high[3]>graph[x][y]: # 이동 방향을 90도 시계 방향으로 회전시킨다.
            if Move==1:
                Move=3
            elif Move==2:
                Move=4
            elif Move==3:
                Move=2
            else:
                Move=1
        elif high[3]<graph[x][y]: #A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
            if Move==1:
                Move=4
            elif Move==2:
                Move=3
            elif Move==3:
                Move=1
            else:
                Move=2
        K-=1

        total += BFS(x,y)
    return total




N,M,K=I_S()

graph=[ L_I() for _ in range(N) ]

print(Dice())
