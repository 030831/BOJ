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

N=I()
ans , count , before_idx , after_idx = 0,0,0,0
dp=[0]*(N+2)
dp[0] = -int(1e9)
dp[N+1] = int(1e9)

L=[0] + LMI()
for i in range(1,N+1):
    dp[i] = L[i]
    if dp[i]<dp[i-1]:
        count+=1
        before_idx = i-1
        after_idx =  i

if count == 0 :
    ans = N
elif count > 1:
    ans = 0
else:
    if dp[before_idx-1] <= dp[after_idx]:
        ans+=1
    if dp[before_idx] <= dp[after_idx+1]:
        ans +=1

print(ans)

"""
1,5,3,4

5 제외 1 , 3, 4
3 제외 1 , 5 , 4
"""