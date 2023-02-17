a=[0]+ list(input().rstrip())
b=[0]+ list(input().rstrip())
high=len(a)
breath=len(b)
dp=[ [""]*breath for i in range(high) ]

string=""
for i in range(1,high):
    for j in range(1,breath):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+a[i]
        else:
            if len(dp[i-1][j])>len(dp[i][j-1]):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]

print(dp[high-1][breath-1])