import sys
input=sys.stdin.readline



N=int(input())
L=list(map(int,input().split()))

M=int(input())
prefix_sum=[0]*(N+1)

for i in range(1,N+1):
    prefix_sum[i]=prefix_sum[i-1]+L[i-1]

for i in range(M):
    a,b=map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])