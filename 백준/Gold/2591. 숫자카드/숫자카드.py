S=list(input())

dp=[0]*(len(S)+1)
dp[0]=dp[1]=1
for i in range(2,len(S)+1):
    if int(S[i-1])>0:
        dp[i]+=dp[i-1]
    if 10<=int(S[i-2])*10+int(S[i-1])<=34:
        dp[i]+=dp[i-2]
print(dp[-1])

