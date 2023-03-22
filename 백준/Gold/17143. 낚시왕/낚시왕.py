import sys
input=sys.stdin.readline
from collections import deque

shark=[ [ deque() for _ in range(101) ] for _ in range(101) ]
shark2=[[deque() for _ in range(101)] for _ in range(101)]


def Delete(idx): # 물고기는 한마리만 잡는다.
    global ans
    for i in range(N):
        if len(shark[i][idx])>0:
            ans+=shark[i][idx][2]
            shark[i][idx].clear()
            return

def Input(K):
    for i in range(K):
        x,y,s,d,z=map(int,input().split())
        shark[x-1][y-1].append(s)
        shark[x-1][y-1].append(d)
        shark[x-1][y-1].append(z)
#입력때 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.

def Move(x,y):
    s,d,z=shark[x][y][0] , shark[x][y][1] , shark[x][y][2]
    if s==0: # 속력이 0 일때
        if len(shark2[x][y])>0:
            if z > shark2[x][y][2]:  # 방문한 지점에 자기가 더 크다면 바꾼다.
                shark2[x][y].append(s)
                shark2[x][y].append(d)
                shark2[x][y].append(z)
            else:  # 방문한 지점에 방문한 상어가 더 크다면 return
                return
        else:
            shark2[x][y].append(s)
            shark2[x][y].append(d)
            shark2[x][y].append(z)
            return

    if d<=2: # 위 아래일 경우
        for i in range(s%((N-1)*2)): # 세로길이의 나머지만큼만 이동한다.
            if d==1:
                if x-1>=0:
                    x-=1
                else:
                    d=2
                    x+=1
            else:
                if x+1<N:
                    x+=1
                else:
                    d=1
                    x-=1
    else: # 오른쪽 왼쪽일 경우\
        for i in range(s%((M-1)*2)): # 가로길이의 나머지만큼만 이동한다.
            if d==3:
                if y+1<M:
                    y+=1
                else:
                    y-=1
                    d=4
            else:
                if y-1>=0:
                    y-=1
                else:
                    y+=1
                    d=3

    if len(shark2[x][y])>0:
        if z>shark2[x][y][2]: # 방문한 지점에 자기가 더 크다면 바꾼다.
            shark2[x][y].clear()
            shark2[x][y].append(s)
            shark2[x][y].append(d)
            shark2[x][y].append(z)
        else: # 방문한 지점에 방문한 상어가 더 크다면 return
            return
    else:
        shark2[x][y].append(s)
        shark2[x][y].append(d)
        shark2[x][y].append(z)

#s는 속력, d는 이동 방향, z는 크기이다.
#d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
def Play():
    global shark
    check=[]
    for i in range(N):
        for j in range(M):
            if len(shark[i][j])>0:
                check.append((i,j))
    for i,j in check:
        Move(i,j)


N,M,K=map(int,input().split())
Input(K)
ans = 0

for _ in range(M):
    Delete(_)
    Play()
    shark = [[deque() for _ in range(101)] for _ in range(101)]
    shark=[ i[:] for i in shark2]
    shark2 = [[deque() for _ in range(101)] for _ in range(101)]

print(ans)