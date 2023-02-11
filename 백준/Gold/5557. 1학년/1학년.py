N=int(input())
L=list(map(int,input().split()))

l=sum(L[:-1])
dp=[ [0]*(l+1) for _ in range(N-1) ]
dp[0][L[0]]+=1

"""
 상근이는 아직 학교에서 음수를 배우지 않았고, 20을 넘는 수는 모른다
"""
for i in range(1,N-1):
    for j in range(l+1):
        if dp[i-1][j]>0:
            if j+L[i]<=20:
                dp[i][j + L[i]]+=dp[i-1][j]
            if j-L[i]>=0:
                dp[i][j-L[i]]+=dp[i-1][j]


print(dp[-1][L[-1]])
