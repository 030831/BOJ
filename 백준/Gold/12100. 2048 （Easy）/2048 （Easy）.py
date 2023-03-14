import sys
input=sys.stdin.readline
from collections import deque
LMI=lambda:list(map(int,input().split()))
MI=lambda:map(int,input().split())
I=lambda:int(input())
G=lambda x:[ LMI() for _ in range(x) ]
V=lambda x,y:[ [False]*y for _ in range(x) ]

def Left(Q,new_graph,x):
    while Q:
        if len(Q) > 1 and Q[0] == Q[1]:
            new_graph[x].append(Q.popleft() * 2)
            Q.popleft()
            continue
        new_graph[x].append(Q.popleft())

    while len(new_graph[x])!=N:
        new_graph[x].append(0)

def Right(Q,new_graph,x):
    while Q:
        if len(Q)>1 and Q[-1]==Q[-2]:
            new_graph[x].appendleft(Q.pop()*2)
            Q.pop()
            continue
        new_graph[x].appendleft(Q.pop())

    while len(new_graph[x])!=N:
        new_graph[x].appendleft(0)

def Up(Q,new_graph):
    y=0
    while Q:
        if len(Q) > 1 and Q[0] == Q[1]:
            new_graph[y].append(Q.popleft() * 2)
            Q.popleft()
            y+=1
            continue
        new_graph[y].append(Q.popleft())
        y+=1

    while y!=N:
        new_graph[y].append(0)
        y+=1

def Down(Q,new_graph):
    y=N-1
    while Q:
        if len(Q)>1 and Q[-1]==Q[-2]:
            new_graph[y].append(Q.pop()*2)
            y-=1
            Q.pop()
            continue
        new_graph[y].append(Q.pop())
        y-=1

    while y!=-1:
        new_graph[y].append(0)
        y-=1

def BackTracking(deep,graph):
    global ans


    if deep==5:
        for i in range(N):
            for j in range(N):
                ans = max(ans , graph[i][j])
        return

    for i in range(4):
        if i==0:
            new_graph = [[] for _ in range(N)]
            for x in range(N):
                Q=deque()
                for y in range(N):
                    if graph[x][y]:
                        Q.append(graph[x][y])
                Left(Q,new_graph,x)
            BackTracking(deep+1,[ i[:] for i in new_graph ])

        elif i==1:
            new_graph = [ deque() for _ in range(N)]
            for x in range(N):
                Q=deque()
                for y in range(N):
                    if graph[x][y]:
                        Q.append(graph[x][y])
                Right(Q,new_graph,x)
            BackTracking(deep+1,[ list(i)[:] for i in new_graph ])

        elif i==2: #위
            new_graph = [[] for _ in range(N)]
            for x in range(N):
                Q=deque()
                for y in range(N):
                    if graph[y][x]:
                        Q.append(graph[y][x])
                Up(Q,new_graph)
            BackTracking(deep+1,[ i[:] for i in new_graph ])

        else: # 아래
            new_graph = [ deque() for _ in range(N)]
            for x in range(N):
                Q=deque()
                for y in range(N):
                    if graph[y][x]:
                        Q.append(graph[y][x])
                Down(Q,new_graph)
            BackTracking(deep+1,[ list(i)[:] for i in new_graph ])

N=I()
graph=G(N)

ans = 0
BackTracking(0,graph)

print(ans)