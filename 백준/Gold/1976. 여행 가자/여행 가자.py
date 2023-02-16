import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def Find(x):

    if disjoint[x]!=x:
        disjoint[x]=Find(disjoint[x])

    return disjoint[x]

def Union(A,B):

    A=Find(A)
    B=Find(B)

    if A>B:
        disjoint[A]=B
    else:
        disjoint[B]=A

N=int(input())
M=int(input())

disjoint=[0]*(N+1)

for i in range(1,N+1):
    disjoint[i]=i

for i in range(N):

    L=list(map(int,input().split()))

    for j in range(len(L)):
        if L[j]==1:
            Union(i+1,j+1)

check=0
Travel=list(map(int,input().split()))

for i in range(len(Travel)):
    if i==0:
        check=Find(Travel[i])
    else:
        if check!=Find(Travel[i]):
            print("NO")
            exit(0)

print("YES")