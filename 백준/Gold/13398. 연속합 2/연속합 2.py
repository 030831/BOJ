import sys
input=sys.stdin.readline

N=int(input())
L=list(map(int,input().split()))

dp=[ [0]*N for _ in range(2) ]
dp[0][0]=L[0]

Answer=-1000
for i in range(1,N):
    dp[0][i]=max(dp[0][i-1]+L[i] , L[i])
    # 제거하지 않을 경우 = 현재값을 선택한것 , 현재값을 선택하지 않은 것 중 최대값
    dp[1][i]=max(dp[1][i-1]+L[i] , dp[0][i-1] )
    #제가혈 경우 = i번째 이전에서 이미 제거하고 값을 더하는경우 , 제거하는 경우중 최대값.
    Answer = max(dp[0][i] , dp[1][i] , Answer)

if N==1:
    print(dp[0][0])
else:
    print(Answer)