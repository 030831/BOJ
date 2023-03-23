import sys
input=sys.stdin.readline
from collections import deque

L_I=lambda:list(map(int,input().split()))
I_S=lambda:map(int,input().split())

def BFS(x,y):

    breath=deque([0,0,0])
    high=deque([0,0,0,0])
    while Move:
        next_Move = Move.popleft()

        if next_Move==1 and y+1<M: #동쪽
            breath[0],high[3],breath[2],high[1]=high[3],breath[2],high[1],breath[0]
            y+=1
        elif next_Move==2 and 0<=y-1: #서쪽
            breath[0],high[1],breath[2],high[3]=high[1],breath[2],high[3],breath[0]
            y-=1
        elif next_Move==3 and 0<=x-1: # 북쪽
            high.appendleft(high.pop())
            x-=1
        elif next_Move==4 and x+1<N: # 남쪽
            high.append(high.popleft())
            x+=1
        else:
            continue
        if graph[x][y]==0: #주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다
            graph[x][y]=high[1]
        else:
            breath[1]=graph[x][y]
            high[1]=graph[x][y]
            graph[x][y]=0
            #0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

        print(high[-1])



N,M,x,y,K=I_S()
graph=[ L_I() for _ in range(N) ]
Move=deque(L_I())


BFS(x,y)