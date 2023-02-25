import sys
input=sys.stdin.readline

def Find(x):
    if x!=disjoint[x]:
        disjoint[x] = Find(disjoint[x])
    return disjoint[x]

def Union(a,b):

    a=Find(a); b=Find(b)

    if a==b:
        return False
    if a>b:
        disjoint[a]=b
    else:
        disjoint[b]=a
    return True

N,M=map(int,input().split())
L=[ [] for _ in range(N+1) ]

for i in range(M):
    a,b=map(int,input().split())
    L[a].append(b)
    L[b].append(a)

disjoint=[ i for i in range(N+1) ]

P=[ int(input()) for _ in range(N)]

P.reverse()
visited=[False]*(N+1)
K=0
answer=["DISCONNECT"]
for i in P:
    K+=1
    for j in L[i]:
        if (visited[j] and Union(j , i)):
            K-=1
    visited[i]=True
    if K==1:
        answer.append("CONNECT")
    else: # 1 이상이라면
        answer.append("DISCONNECT")


for i in answer[::-1]:
    print(i)