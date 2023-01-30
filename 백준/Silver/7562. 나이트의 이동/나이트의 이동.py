from collections import deque
import sys
input=sys.stdin.readline

dx=[-2,-1,1,2,1,2,-2,-1]
dy=[1,2,2,1,-2,-1,-1,-2]

T=int(input())

for i in range(T):
    count = []
    graph=[]
    P=int(input())
    graph=[ [0]*P for _ in range(P)]

    A1,B1=map(int,input().split())
    graph[A1][B1]=1
    A2,B2=map(int,input().split())
    graph[A2][B2]=-1

    visit= [ [False]*P for _ in range(P)] ; deq=deque()

    def BFS(x,y):
        global count

        visit[x][y]=True
        deq.append([x,y])

        while deq:
            x,y=deq.popleft()
            for i in range(8):
                A=x+dx[i] ; B=y+dy[i]
                if 0<=A<P and 0<=B<P:
                    if graph[A][B]==0 and not visit[A][B]:
                        graph[A][B]=graph[x][y]+1
                        visit[A][B]=True
                        deq.append([A,B])
                    elif graph[A][B]==-1:
                        count.append(graph[x][y]+1)

    BFS(A1,B1)
    print(min(count)-1)

