import sys
input=sys.stdin.readline

L=list()

a,b=map(int,input().split())
for i in range(a):
    L.append(int(input()))
L.sort()
start=1
end=L[-1]

while start<=end:
    mid = (end + start) // 2
    count=0
    for i in range(len(L)):
        count+=L[i]//mid
    if count>=b:
        start=mid+1
    elif count<b:
        end=mid-1

print(end)
