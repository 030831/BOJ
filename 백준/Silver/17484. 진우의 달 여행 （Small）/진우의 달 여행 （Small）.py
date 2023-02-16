import sys
input=sys.stdin.readline
INF = 1000000
N,M=map(int,input().split())

dp=[ [ [0]*3 for _ in range(M) ] for _ in range(N) ]

L=[ list(map(int,input().split())) for _ in range(N) ]

for i in range(M):
    for j in range(3):
        dp[0][i][j] = L[0][i]

for i in range(1,N):
    for j in range(M):
        for k in range(3):
            if  (j == 0 and k == 0) or (j == M - 1 and k == 2): # 같은 방향으로 두번 이동할 수 없다.
                dp[i][j][k] = INF
                continue
            if k==0:
                dp[i][j][k] = min(dp[i-1][j-1][1] , dp[i-1][j-1][2]) + L[i][j]
                # K = 0 일때는 왼쪽에서 오는 경우
            elif k==1:
                dp[i][j][k] = min(dp[i-1][j][0] , dp[i-1][j][2]) + L[i][j]
                #  K =1 일때는 중앙으로 오는경우
            else:
                dp[i][j][k] = min(dp[i-1][j+1][0] , dp[i-1][j+1][1]) + L[i][j]
                # K = 2 일떄는 오른쪽으로 오는 경우
result = INF
for i in range(M):
    result = min(result, min(dp[-1][i]))

print(result)

