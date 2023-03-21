import sys
input=sys.stdin.readline

for _ in range(int(input())):

    N=int(input())
    L=[ [0,0] + list(map(int,input().split())) for _ in range(2)  ]
    L.insert(0 , [0]*(N+2) )
    dp=[ [0]*(N+2) for _ in range(3) ]

    for i in range(2,N+2):
        dp[1][i] = max(L[1][i] + L[2][i-1] + dp[1][i-2] , dp[1][i-1] , L[1][i] + dp[2][i-1] )
        dp[2][i] = max(L[2][i] +  L[1][i-1] + dp[2][i-2]  , dp[2][i-1] , L[2][i] + dp[1][i-1])

    print(max(dp[1][-1] , dp[2][-1]))
"""
1
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80

10 30 30 80 130 130 170
20 50 80 130 210 210 290


1
5
50 10 100 20 40
30 50 70 10 60
"""
