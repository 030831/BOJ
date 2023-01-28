import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

N=int(input())

Tree=[ [] for _ in range(N+1) ]
Parents=[ 0 for _ in range(N+1) ]

for i in range(N-1):
    a,b=map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)


def DFS(start,Tree,parents):

    for i in Tree[start]:
        if Parents[i]==0:
            Parents[i]=start
            DFS(i,Tree,parents)

DFS(1,Tree,Parents)

for i in range(2,N+1):
    print(Parents[i])