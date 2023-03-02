import sys,copy
input = sys.stdin.readline
from collections import deque

def Camera_index():
    for i in range(N):
        for j in range(M):
            if 1 <= graph[i][j] <= 5:
                Camera.append((i, j, graph[i][j]))

def Left(Camera_graph,x,y):
    while y >= 0:
        if Camera_graph[x][y] != 6:
            if Camera_graph[x][y] == 0:
                Camera_graph[x][y] = -1
            y -= 1
        else:
            return
def Right(Camera_graph,x,y):
    while y < M:
        if Camera_graph[x][y] != 6:
            if Camera_graph[x][y] == 0:
                Camera_graph[x][y] = -1
            y += 1
        else:
            return

def Up(Camera_graph,x,y):
    while x >= 0:
        if Camera_graph[x][y] != 6:
            if Camera_graph[x][y] == 0:
                Camera_graph[x][y] = -1
            x -= 1
        else:
            return

def Down(Camera_graph,x,y):
    while x < N:
        if Camera_graph[x][y] != 6:
            if Camera_graph[x][y] == 0:
                Camera_graph[x][y] = -1
            x += 1
        else:
            return
def Find(Camera_graph):
    total=0
    for i in range(N):
        for j in range(M):
            if Camera_graph[i][j]==0:
                total+=1
    return total

def BFS(Q):

    Q=deque(Q)
    Camera_graph=copy.deepcopy(graph)
    # 방향 1 : 동 , 2: 남 , 3 : 서 , 4 : 북
    while Q:
        direction,x,y,favor=Q.popleft()
        if favor==1:
            if direction==1:
                Right(Camera_graph,x,y)
            elif direction==2:
                Down(Camera_graph,x,y)
            elif direction==3:
                Left(Camera_graph,x,y)
            elif direction==4:
                Up(Camera_graph,x,y)
        elif favor==2:
            if direction%2==0:
                Right(Camera_graph,x,y)
                Left(Camera_graph, x, y)
            else:
                Up(Camera_graph, x, y)
                Down(Camera_graph, x, y)
        elif favor==3:
            if direction==1:
                Up(Camera_graph, x, y)
                Right(Camera_graph, x, y)
            elif direction==2:
                Right(Camera_graph, x, y)
                Down(Camera_graph, x, y)
            elif direction==3:
                Down(Camera_graph, x, y)
                Left(Camera_graph, x, y)
            else:
                Left(Camera_graph, x, y)
                Up(Camera_graph, x, y)
        elif favor==4:
            if direction==1:
                Left(Camera_graph, x, y)
                Up(Camera_graph, x, y)
                Right(Camera_graph, x, y)
            elif direction==2:
                Up(Camera_graph, x, y)
                Right(Camera_graph, x, y)
                Down(Camera_graph, x, y)
            elif direction==3:
                Right(Camera_graph, x, y)
                Down(Camera_graph, x, y)
                Left(Camera_graph, x, y)
            else:
                Down(Camera_graph, x, y)
                Left(Camera_graph, x, y)
                Up(Camera_graph, x, y)
        elif favor==5:
            Down(Camera_graph, x, y)
            Left(Camera_graph, x, y)
            Right(Camera_graph,x,y)
            Up(Camera_graph, x, y)

    return Find(Camera_graph)


def Back_Tracking():
    global total

    if len(P) == len(Camera):
        total += 1
        for i in range(len(P)):
            L[total].append((P[i],Camera[i][0],Camera[i][1],Camera[i][2]))
        return

    for i in range(1,5):
        P.append(i)
        Back_Tracking()
        P.pop()

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
Camera = [] ; Camera_index()
L = [ [] for _ in range(65537)] ; P=[]
total = 0
check=int(1e9)
Back_Tracking()
Camera.clear()

for i in range(1,total+1):
    check=min(check , BFS(L[i]) )
print(check)