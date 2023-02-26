from collections import deque
import sys
input=sys.stdin.readline


"""
0 - 오른쪽 , 1 = 아래 , 2 = 왼쪽 , 3 = 위쪽
"""
def BFS():

    time = 0 ; Q=deque() ; visit=deque()
    Q.append([0,0,0])
    visit.append([0,0])

    while Q:


        a,b,direction=Q.popleft()

        if L and time == L[0][0]:
            if L[0][1]=='D':
                direction+=1 # 오른쪽으로 90도
                if direction==4:
                    direction=0
            else:
                direction-=1 # 왼쪽으로 90도
                if direction==-1:
                    direction=3
            L.popleft()

        if direction==0:
            nx,ny=a,b+1
        elif direction==1:
            nx,ny=a+1,b
        elif direction==2:
            nx,ny=a,b-1
        elif direction==3:
            nx,ny=a-1,b

        if 0<=nx<N and 0<=ny<N:
            Q.append([nx,ny,direction])
            if graph[nx][ny]==-1:
                graph[nx][ny]=graph[a][b]+1
                visit.append([nx, ny])
            elif graph[nx][ny]==0:
                A,B=visit.popleft()
                graph[nx][ny] = graph[a][b] + 1
                graph[A][B]=0
                visit.append([nx, ny])
            elif graph[nx][ny]!=0:
                break
        else:
            break # 종료

        time +=1


N=int(input())
graph=[ [0]*N for _ in range(N) ]

for i in range(int(input())):
    a,b=map(int,input().split())
    graph[a-1][b-1]=-1
graph[0][0]=1
L=deque()

for i in range(int(input())):
    time , direction = input().split()
    L.append([int(time) , direction])


BFS()

answer=0
for i in range(N):
    for j in range(N):
        answer=max(answer,graph[i][j])
print(answer)