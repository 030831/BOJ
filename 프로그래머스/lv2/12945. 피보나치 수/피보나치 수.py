def solution(n):
    dp=[0,1]
    
    for i in range(n):
        dp.append( (dp[-1]+dp[-2])% 1234567)
    return dp[n]%1234567