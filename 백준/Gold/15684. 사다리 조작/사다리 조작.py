"""
30C1 = 30
30C2 = 435
30C3 = 4060

최대개 30 개의 사다리중에 사다리를 1 , 2 , 3개 고르는 모든 경우의 수를 골라서 브루트 포스로 탐색한다.
[2, 1, 4, 3, 0]
[0, 0, 4, 3, 0]
[0, 3, 2, 5, 4]
[0, 3, 2, 0, 0]
[2, 1, 0, 5, 4]
[0, 0, 0, 0, 0]
높이가 H 임. M 은 원래 상태에 있는 사다리의 개수.
Ladder_graph=[ i[:] for i in graph]
슬라이싱 복다가 deepcopy 보다 시복도가 엄청 빠르다.
"""

import sys
input=sys.stdin.readline
from itertools import combinations

LMI=lambda:list(map(int,input().split()))
MI=lambda:map(int,input().split())
G=lambda x:[ LMI() for _ in range(x) ]
V=lambda x,y:[ [False]*y for _ in range(x) ]


def Ladder(P):
    Ladder_graph=[ i[:] for i in graph]

    for x,y in P:
        Ladder_graph[x][y]=y+2
        Ladder_graph[x][y+1]=y+1

    total = 0

    for i in range(N):
        x,y=[0,i]
        while True:
            if x==H:
                if y==i:
                    total+=1
                    break
                else:
                    return False
            if Ladder_graph[x][y]:
                y=Ladder_graph[x][y]-1
                x+=1
            else:
                x+=1
    if total==N:
        return True
    return False

N,M,H=MI()
graph=[ [0]*N for _ in range(H+1) ]
L=[] ; P=[]
for i in range(M):
    a,b=MI()
    graph[a-1][b]=b
    graph[a-1][b-1]=b+1

for i in range(H+1):
    for j in range(1,N):
        if [graph[i][j-1],graph[i][j]]==[0,0]:
            L.append((i,j-1))


if Ladder([]):
    print(0)
    exit(0)

for i in range(len(L)):
    if Ladder([L[i]]):
        print(1)
        exit(0)

for i in combinations(L, 2):
    if Ladder(i):
        print(2)
        exit(0)
for i in combinations(L,3):
    if Ladder(i):
        print(3)
        exit(0)

print(-1)