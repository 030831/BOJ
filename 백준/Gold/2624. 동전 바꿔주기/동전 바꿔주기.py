import sys
input=sys.stdin.readline

T=int(input())
K=int(input())

coins = [ list(map(int,input().split())) for _ in range(K) ]
dp=[0]*(T+1)
dp[0]=1

for coin,cnt in coins:
    for i in range(T,0,-1):
        for j in range(1,cnt+1):
            if i-coin*j>=0:
                dp[i] += dp[i-coin*j]


print(dp[T])