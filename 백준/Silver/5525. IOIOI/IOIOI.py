import sys
input=sys.stdin.readline

String=[]

String.append("I")

N=int(input())

for i in range(N):
    String.append("O")
    String.append("I")

M=int(input())
L=list(input().rstrip())

start=0 ; end=1

P=[] ; P.append(L[start]) ; P.append(L[end])

total=0
while end<M:

    if len(P)<len(String):
        end+=1
        P+=L[end]

    elif len(P)==len(String):
        if P==String:
            total+=1

        if end==M-1:
            break
        P=P[1:]
        start+=1 ; end+=1
        P+=L[end]

print(total)