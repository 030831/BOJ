import sys
input=sys.stdin.readline
MAX = 500001
LOG = 19

M=int(input())
Parent=[ [0]*LOG for _ in range(MAX) ]

L=list(map(int,input().split()))

for i in range(1,M+1):
    Parent[i][0] = L[i-1]

for i in range(1,LOG):
    for j in range(1,M+1):
        Parent[j][i]=Parent[Parent[j][i-1]][i-1]

Q=int(input())

for i in range(Q):
    N,X=map(int,input().split())

    for i in range(LOG-1,-1,-1):
        if N>=(1<<i):
            N-=(1<<i)
            X=Parent[X][i]

    print(X)