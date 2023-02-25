N=int(input())
L=list(map(int,input().split()))
P=int(1e9)
ans=0
for i in range(N):
    P=min(L[i] , P)
    ans=max(ans,L[i]-P)
print(ans)
