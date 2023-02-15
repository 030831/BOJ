import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)


def DFS(node , deep):
    visit[node]=True
    Depth[node] = deep

    for i in graph[node]:
        if not visit[i]:
            Parent[i]=node # 부모 인덱스에 자식값을 저장한다.
            DFS(i , deep+1)

def LCA(a,b):

    while Depth[a]!=Depth[b]: # 두 노드의 깊이가 같을 때 까지
        if Depth[a]>Depth[b]:
            a=Parent[a] # a 가 더 깊다면 a는 부모 노드로 올라간다.
        else:
            b=Parent[b]

    while a!=b: # 두 노드가 같아질때까지
        a=Parent[a]
        b=Parent[b]

    return a

N=int(input())

Parent=[0]*(N+1)
Depth=[0]*(N+1)
visit=[False]*(N+1)

graph=[ [] for _ in range(N+1) ]
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    Parent[b] = a
    #한 간선 당 한 줄에 두 개의 숫자 A B 가 순서대로 주어지는데, 이는 A가 B의 부모라는 뜻입니다.


DFS(1,0)

for i in range(int(input())):
    a,b=map(int,input().split())

    print(LCA(a,b))
