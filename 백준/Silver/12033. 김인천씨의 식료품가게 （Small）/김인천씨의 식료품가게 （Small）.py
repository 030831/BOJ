for i in range(int(input())):
    N=int(input())
    L=list(map(int,input().split()))

    P=[False]*(2*N)

    for j in range(2*N):
        if not P[j]:
            for k in range(j+1,2*N):
                if not P[k]:
                    if L[j]==int(L[k]*0.75):
                        P[k]=True
                        break

    tmp=[]
    for j in range(len(P)):
        if P[j]:
            tmp.append(int(L[j]*0.75))
    print("Case #%d: " % (i + 1), end="")
    print(*tmp)