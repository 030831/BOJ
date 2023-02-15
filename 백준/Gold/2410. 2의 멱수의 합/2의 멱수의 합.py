N=int(input())

dp=[0]*(N+1)
dp[0]=1

L=[ 2**i for i in range(21) ]

for i in L:
    if i<=N:
        for j in range(i,N+1):
            dp[j] += dp[j-i]%1000000000
print(dp[N]%1000000000)