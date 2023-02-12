import sys
input=sys.stdin.readline

N,M=map(int,input().split())
K=int(input())

dp=[ [0]*(M+1) for _ in range(N+1) ]
visit=set()

for i in range(K):
    a,b,c,d=map(int,input().split())
    if a>c or b>d:
        visit.add((c,d,a,b))
    else:
        visit.add((a,b,c,d))

dp[0][0]=1

for i in range(N+1):
    for j in range(M+1):
        if i==0 and j==0:
            continue
        if i==0 and (i,j-1,i,j) not in visit:
            dp[i][j]=dp[i][j-1]
        if j==0 and (i-1,j,i,j) not in visit:
            dp[i][j]=dp[i-1][j]
        elif i>0 and j>0:
            if (i,j-1,i,j) not in visit and (i-1,j,i,j) not in visit:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            elif (i-1,j,i,j) not in visit:
                dp[i][j]=dp[i-1][j]
            elif (i,j-1,i,j) not in visit:
                dp[i][j]=dp[i][j-1]


print( dp[N][M] )