N,S,M=map(int,input().split()) # 곡의 개수 , 시작 볼륨 , 최대값


L=list(map(int,input().split()))
dp=[ [0]*1001 for _ in range(N+1) ]
dp[0][S]=1

for i in range(1,N+1):

    for j in range(1001):
        if dp[i-1][j]==1 and j-L[i-1]>=0:
            dp[i][j-L[i-1]]=1

        if dp[i-1][j]==1 and j+L[i-1]<=M:
            dp[i][j+L[i-1]]=1


index = -1

for i in range(M+1):
    if dp[N][i]==1:
        index=i
print(index)