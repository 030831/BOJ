N=int(input())
L=list(map(int,input().split()))

dp=[0]*(N+1)

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i] , dp[j-1]+max(L[i-1],L[j-1]) - min(L[i-1] , L[j-1]))
        # i 번째 선택한 값 = 자기자신 , 이전의 dp 값 + max(i-1번째 리스트값 , j-1번째 리스트값) - min(i-1번째 리스트값 , j-1번째 리스트값)
print(dp[N])