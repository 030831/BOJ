import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    coin=int(input())
    L=list(map(int,input().split()))
    W=int(input())
    dp=[0]*(W+1)

    dp[0]=1
    
    for i in range(len(L)):
        for j in range(1,W+1):
            if j>=L[i]:
                dp[j]+=dp[j-L[i]]
    print(dp[W])