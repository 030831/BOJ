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

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

def getNumber(number  , newGraph):
    for i in range(4):
        for j in range(4):
            if newGraph[i][j][0]==number:
                return i,j,newGraph[i][j][1]
    return -1,-1,-1

def move(newGraph):

    number = 1
    while True:
        x,y,direction=-1,-1,-1
        while [x,y,direction]==[-1,-1,-1]: # 17이 아니라 18로 해야함.
            x,y , direction= getNumber(number,newGraph)
            number+=1
            if number >= 19:
                return
        if number>=19:
            return

        nx,ny = x+dx[direction] , y+dy[direction]
        spinCount = 0

        while nx<0 or nx>3 or ny<0 or ny>3 or newGraph[nx][ny][0]==0:
            direction+=1
            spinCount += 1
            if direction==8:
                direction=0
            nx,ny = x+dx[direction] , y+dy[direction]

            if spinCount>10:
                break

        if spinCount>10:
            pass
        else:
            if newGraph[nx][ny]==[-1,-1]: # 빈칸은 스왑
                newGraph[nx][ny] = [ newGraph[x][y][0] , direction]
                newGraph[x][y] = [ -1 , -1]
            else:
                P=[ newGraph[x][y][0] , direction ]
                newGraph[x][y] = [ newGraph[nx][ny][0] , newGraph[nx][ny][1] ]
                newGraph[nx][ny] = P

def backTracking(coin , graph):
    global total
    total = max(total, coin)



    newGraph=[ i[:] for i in graph]

    move(newGraph)

    check = 0

    for i in range(4):
        for j in range(4):
            if newGraph[i][j][0] == 0:
                x,y,direction = i , j , newGraph[i][j][1]
            if newGraph[i][j][0] > 0:
                check+=1

    if not check:
        return

    nx,ny = x,y
    check = 0

    for i in range(4):
        nx+=dx[direction] ; ny+=dy[direction]
        if 0<=nx<4 and 0<=ny<4 and newGraph[nx][ny]!=[-1,-1]:

            coinPlus = newGraph[nx][ny][0]
            coin += coinPlus
            delete = newGraph[nx][ny]
            shark = newGraph[x][y]
            newGraph[nx][ny]= [0 , newGraph[nx][ny][1] ]
            newGraph[x][y] = [-1,-1]
            check+=1


            backTracking(coin , newGraph)

            newGraph[nx][ny] = delete
            newGraph[x][y] = shark
            coin -= coinPlus

    if not check:
        return

graph=[ [] for _ in range(4) ]

for i in range(4):
    L=LMI()
    for j in range(0,8,2):
        graph[i].append([L[j] , L[j+1]-1])


startCoin = graph[0][0][0]
graph[0][0] = [0 , graph[0][0][1]]
total = startCoin

backTracking(startCoin, graph)

print(total)

