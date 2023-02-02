N=int(input())

L=list(map(int,input().split()))

L.sort(key=lambda x:-x)

total=0
for i in range(N):
    total=max(total , i+2+L[i])

print(total)