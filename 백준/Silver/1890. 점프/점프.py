import sys
input=sys.stdin.readline

N=int(input())

graph=[ list(map(int,input().split())) for _ in range(N) ]

dp=[ [0]*N for _ in range(N) ]

if graph[0][0]!=0:
    dp[0][0]=1

for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1:
            continue
        if j+graph[i][j]<N:
            dp[i][j+graph[i][j]]+=dp[i][j]
        if i+graph[i][j]<N:
            dp[i+graph[i][j]][j]+=dp[i][j]


print(dp[N-1][N-1])


"""

9
3 1 2 2 3 3 1 1 2
1 1 2 1 1 2 3 1 2
2 1 1 3 2 2 1 3 1
3 3 1 1 1 3 1 2 1
3 2 2 2 1 1 3 3 1
3 1 3 2 2 3 1 3 3
3 1 1 2 1 1 1 1 1
2 3 1 3 1 3 2 2 2
3 3 3 2 3 1 3 3 0

ans  =6
"""