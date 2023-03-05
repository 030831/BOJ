import sys
input=sys.stdin.readline
from collections import deque

LMI=lambda:list(map(int,input().split()))
MI=lambda:map(int,input().split())
I=lambda:int(input())
G=lambda x:[ LMI() for _ in range(x) ]
V=lambda x,y:[ [False]*y for _ in range(x) ]

"""
봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
"""
def Spring():
    dead.clear()
    for i in range(N):
        for j in range(N):
            idx=0
            for k in range(len(tree[i][j])):
                if ground[i][j]>=tree[i][j][k]:
                    ground[i][j]-=tree[i][j][k]
                    tree[i][j][k]+=1
                    idx+=1
                else:
                    break

            for k in range(len(tree[i][j])-idx):
                ground[i][j]+=tree[i][j][-1]//2
                tree[i][j].pop()

"""
여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 
각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
"""

"""
가을에는 나무가 번식한다. 
번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
"""

def Fall():
    P=[]
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k]%5==0:
                    for _ in range(8):
                        nx,ny=i+dx[_],j+dy[_]
                        if 0<=nx<N and 0<=ny<N:
                            P.append((nx,ny))

    for x,y in P:
        tree[x][y].appendleft(1)

"""
겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 
각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
"""
def Winter():
    for i in range(N):
        for j in range(N):
            ground[i][j] += graph[i][j]

def Alive():
    total=0
    for i in range(N):
        for j in range(N):
            total+=len(tree[i][j])
    return total

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
N,M,K=MI()
graph=G(N)
tree=[ [ deque() for _ in range(N)] for _ in range(N)]
dead=[]
for i in range(M):
    x,y,z=MI()
    tree[x-1][y-1].append(z)
ground=[ [5]*N for _ in range(N) ] #가장 처음에 양분은 모든 칸에 5만큼 들어있다.

for i in range(K):
    Spring()
    Fall()
    Winter()
print(Alive())
