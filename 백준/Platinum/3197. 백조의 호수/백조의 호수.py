from collections import deque
import sys
input=sys.stdin.readline

"""
1. 백조를찾는 Swans 함수.

deq3에서는 백조를 기점으로 다른 백조를 찾는 BFS 를 한다.
이때 graph가 물일때는 deq3에 원소를 추가하여 계속 탐색한다

만약 얼음일떄는 deq4에 원소를 추가한다.

백조를 만났을떄는 원소를 추가해주고 매번방문처리를 해준다.

만약 deq3의 원소가 0개라면
deq4의 원소를 deq3으로 이전해준다.

2. 얼음을 녹이는 BFS 함수

이 함수는 하나만 고려해주면된다.
deq에 처음에 모든 물의 위치를 저장한 후
만약 graph가 얼음이라면
deq2에 좌표를 추가해준다.

이후 deq의 원소가 0 개라면
deq2의 원소를 deq로 이전해준다.

백조가 있는 위치도 주위에 얼음이 녹는다.

"""

def Swans():
    global Find,deq3
    deq4 = deque()

    while deq3:
        x,y=deq3.popleft()
        for i in range(4):
            nx = x + dx[i] ; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == "." and not visit_Swans[nx][ny]:
                    visit_Swans[nx][ny] = True
                    deq3.append([nx, ny])
                elif graph[nx][ny]=="X" and not visit_Swans[nx][ny]:
                    visit_Swans[nx][ny]=True
                    deq4.append([nx,ny])
                elif graph[nx][ny]=="L" and not visit_Swans[nx][ny]:
                    Find=True
                    break
    deq3=deq4

def BFS():
    global deq
    Length=len(deq)
    for _ in range(Length):
        x,y=deq.popleft()
        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]=="X" and not visit[nx][ny]:
                    graph[nx][ny]='.'
                    visit[nx][ny]=True
                    deq.append([nx,ny])




dx=[-1, 0 , 0, 1]
dy=[0, -1 , 1 , 0]

N,M=map(int,input().split())

graph=[ list(input().rstrip()) for _ in range(N) ]
deq=deque()

labudovi=[]
visit=[ [False]*M for _ in range(N) ]
visit_Swans=[ [False]*M for _ in range(N) ]
for i in range(N):
    for j in range(M):
        if graph[i][j]!="X":
            deq.append([i,j])
        if graph[i][j]=="L":
            labudovi.append([i,j])

deq3=deque()
deq3.append([labudovi[0][0] , labudovi[0][1]])

visit_Swans[labudovi[0][0]][labudovi[0][1]]=True

Find=False
Day=0
while Find==False:
    Swans()
    if Find==False:
        BFS()
        Day+=1

print(Day)
