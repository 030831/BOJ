N,K=map(int,input().split())
L=list(map(int,input().split()))

total=0
def BackTracking(stack):
    global total

    if len(stack)!=0:
        check=''.join(stack)
        check=int(check)
        if check<=N and stack[0]!="0":
            total = max(total , int(stack))

    for i in range(K):
        if len(stack)<len(str(N)):
            stack+=str(L[i])
            BackTracking(stack)
            stack=list(stack)
            stack.pop()
            stack=''.join(stack)

BackTracking("")
print(total)