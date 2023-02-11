import sys
input=sys.stdin.readline

N=int(input())
L=[ list(map(int,input().split())) for _ in range(N) ]
dp=[0]*(N+1001)

for i in range(N):
    dp[i]=max(dp[i],dp[i-1]) # 선택하지 않는 경우.
    dp[i+L[i][0]]=max(dp[i]+L[i][1], dp[i+L[i][0]]) # 선택할 경우
    # 다음에 일할 위치 = 현재 위치 + 보수 , 자기자신 중 최대값.

print( max(dp[:N+1]))