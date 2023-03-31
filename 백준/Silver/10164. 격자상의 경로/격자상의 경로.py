N,M,K=map(int,input().split())

dp=[ [0]*(M+1) for _ in range(N+1)]

dp[1][1] =1

if K:
    check_x,check_y = K//M+1,K%M
else:
    check_x,check_y = -1,-1

for i in range(1,N+1):
    for j in range(1,M+1):
        if i<check_x and j>check_y:
            continue
        if i>check_x and j<check_y:
            continue
        else:
            dp[i][j] = max(dp[i][j] , dp[i-1][j]+dp[i][j-1])

print(dp[-1][-1])