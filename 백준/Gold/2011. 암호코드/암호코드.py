N=list(input())

l=len(N)
dp=[0]*(l+1)
dp[0]=dp[1]=1

if N[0]=="0":
    print(0)
else:
    for i in range(2,l+1):
        if int(N[i-1])>0:
            dp[i]+=dp[i-1]
        t= int(N[i-2])*10 + int(N[i-1])
        if 10<=t<=26:
            dp[i]+=dp[i-2]
    print(dp[-1]%1000000)

