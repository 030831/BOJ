N,S=map(int,input().split())
L=list(map(int,input().split()))

value=[] ; total=0

visit=[False]*N
def BackTracking(start,value):

    global total
    if sum(value)==S and len(value)>0:
        total+=1

    for i in range(start,N):
        if not visit[i]:
            value.append(L[i])
            visit[i]=True
            BackTracking(i,value)
            value.pop()
            visit[i]=False

BackTracking(0,value)
print(total)