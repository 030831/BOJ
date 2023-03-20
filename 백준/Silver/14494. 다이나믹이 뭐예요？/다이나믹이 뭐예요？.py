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

N,M=MI()
dp=[ [0]*(M+1) for _ in range(N+1) ]

dp[1][1] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max( dp[i][j] ,dp[i-1][j-1] +dp[i-1][j]+dp[i][j-1] )%1000000007

print(dp[-1][-1]%1000000007)