import sys
input=sys.stdin.readline

L_I=lambda:list(map(int,input().split()))

N=int(input())

L = L_I()

B,C=map(int,input().split())
total = 0

for i in range(N):
    L[i]-=B ; total+=1

    if L[i]>0:
        total+=L[i]//C
        if L[i]%C!=0:
            total+=1


print(total)