import sys
input=sys.stdin.readline

N=int(input())

# dp[i][j] => 왼쪽카드더미(left)에서 -i장 버리고, 오른쪽 카드더미(right) 중에 -j장 버렸을때 최댓값이다.
left =  list(map(int,input().split()))
right = list(map(int,input().split()))

dp=[ [0]*(N+1) for _ in range(N+1)]

for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        if left[i]>right[j]: # 오른쪽 카드가 값이 더 작다면 점수를 얻을 수 있다.
            dp[i][j] = max(dp[i][j+1]+right[j] , dp[i+1][j] , dp[i+1][j+1])
        else:
            dp[i][j] = max(dp[i+1][j] , dp[i+1][j+1])


print(dp[0][0])