import sys
input=sys.stdin.readline

N=int(input())
L=[ int(input()) for i in range(N)]
stack=[(0,L[0])]
L.append(0)
count=0

for i in range(1,N+1):
    check=i
    while stack and stack[-1][1]>L[i]:   
        check,high=stack.pop()
        count=max(count, high*(i-check))
    stack.append((check,L[i]))
print(count)