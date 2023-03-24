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
dy=[0,1,1,1,0,-1,-1,-1]

def move():
    global visit
    visit = [[list() for _ in range(N)] for _ in range(N)]
    for i in range(len(shark)):
        x,y,m,s,d  = shark[i]
        for j in range(s%N):
            x+=dx[d];y+=dy[d]
            #격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
            if x==N:
                x=0
            if x==-1:
                x=N-1
            if y==N:
                y=0
            if y==-1:
                y=N-1
        shark[i] = x,y,m,s,d
        visit[x][y].append((x,y,m,s,d))

def delete(x,y):
    idx = 0
    while idx<len(shark):
        if shark[idx][0]==x and shark[idx][1]==y:
            del shark[idx]
            continue
        idx+=1

def findShark():
    for i in range(N):
        for j in range(N):
            if len(visit[i][j])>1:
                combine(i,j)

def combine(i,j):
    newM,newS,odd,even = 0,0,0,0
    for x,y,m,s,d in visit[i][j]:
        newM+=m ; newS+=s
        if d%2==0:
            even+=1
        else:
            odd+=1

    newM//=5 ; newS//=len(visit[i][j])

    if even==len(visit[i][j]) or odd==len(visit[i][j]):
        direction=[0,2,4,6]
    else:
        direction=[1,3,5,7]

    delete(i,j)

    if newM>0:
        for k in range(4):
            shark.append([i,j,newM,newS,direction[k]])




N,M,K=MI()
shark=[]
visit=[ [ list() for _ in range(N) ] for _ in range(N) ]
for i in range(M):
    x,y,m,s,d=MI()
    shark.append([x-1,y-1,m,s,d])

for i in range(K):
    move()
    findShark()
ans = 0

for i in range(len(shark)):
    ans += shark[i][2]
print(ans)
