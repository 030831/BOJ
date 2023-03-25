N,M=map(int,input().split())

L=list(map(int,input().split()))
start=0
end=0
count=0
while start<=end and end<=N:
    total=sum(L[start:end])
    if total==M:
        count+=1
        end+=1
    elif total<M:
        end+=1
    else:
        start+=1

print(count)