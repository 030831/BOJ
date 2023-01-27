from collections import deque

def BFS():
    deq=deque()
    deq.append([N1,N2])

    visit[N1][N2]=1

    while deq:
        x,y=deq.popleft()

        if x==M1 and y==M2:
            return visit[x][y]-1

        if 0<=x-3<=9 and 0<=y-2<=8 and not visit[x-3][y-2]:
            if (x-1==M1 and y==M2) or (x-2==M1 and y-1==M2):
                pass
            else:
                visit[x-3][y-2]=visit[x][y]+1
                deq.append([x-3,y-2])

        if 0<=x-2<=9 and 0<=y-3<=8 and not visit[x-2][y-3]:
            if (x==M1 and y-1==M2) or (x-1==M1 and y-2==M2):
                pass
            else:
                visit[x-2][y-3]=visit[x][y]+1
                deq.append([x-2,y-3])

        if 0<=x+2<=9 and 0<=y-3<=8 and not visit[x+2][y-3]:
            if (x==M1 and y-1==M2) or (x+1==M1 and y-2==M2):
                pass
            else:
                visit[x+2][y-3]=visit[x][y]+1
                deq.append([x+2,y-3])

        if 0<=x+3<=9 and  0<=y-2<=8 and not visit[x+3][y-2]:
            if (x+1==M1 and y==M2) or (x+2==M1 and y-1==M2):
                pass
            else:
                visit[x+3][y-2]=visit[x][y]+1
                deq.append([x+3,y-2])

        if 0<=x-3<=9 and 0<=y+2<=8 and not visit[x-3][y+2]:
            if (x-1==M1 and y==M2) or (x-2==M1 and y+1==M2):
                pass
            else:
                visit[x-3][y+2]=visit[x][y]+1
                deq.append([x-3,y+2])

        if 0<=x-2<=9 and 0<=y+3<=8 and not visit[x-2][y+3]:
            if (x==M1 and y+1==M2) or (x-1==M1 and y+2==M2):
                pass
            else:
                visit[x-2][y+3]=visit[x][y]+1
                deq.append([x-2,y+3])

        if 0<=x+2<=9 and 0<=y+3<=8 and not visit[x+2][y+3]:
            if (x==M1 and y+1==M2) or (x+1==M1 and y+2==M2):
                pass
            else:
                visit[x+2][y+3]=visit[x][y]+1
                deq.append([x+2,y+3])

        if 0<=x+3<=9 and 0<=y+2<=8 and not visit[x+3][y+2]:
            if (x+1==M1 and y==M2) or (x+2==M1 and y+1==M2):
                pass
            else:
                visit[x+3][y+2]=visit[x][y]+1
                deq.append([x+3,y+2])


N1,N2=map(int,input().split())
M1,M2=map(int,input().split())

visit=[ [0]*9 for _ in range(10) ]

print( BFS() )