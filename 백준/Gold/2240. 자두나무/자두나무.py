import sys
input=sys.stdin.readline

T,W=map(int,input().split())

L=[ int(input()) for _ in range(T) ]

dp=[ [0]*(W+1) for _ in range(T) ]

# dp[i][j] ; i = 고려할 수 있는 사과 ; j = W번까지 이동했을때의 최대값.

for i in range(T):
    for j in range(W+1):
        if j==0: # 초기값
            if L[i]==1: # 시작위치가 1 이라면
                dp[i][0]=dp[i-1][0]+1 # 처음시작위치는 1 이기때문에 +1
            else:
                dp[i][0]=dp[i-1][0] # 처음시작위치와 다르므로 이전값을 가진다.
        else:
            if L[i]==1 and j%2==0: # 사과가 1일때 짝수의 시간일때만 받을 수 있다. 시작위치가 1 이기 때문.
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-1]) +1
            elif L[i]==2 and j%2==1:
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-1])

print(max(dp[-1]))