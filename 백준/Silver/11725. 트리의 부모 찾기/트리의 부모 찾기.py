import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(node):

    for i in Tree[node]:
        if dp[i]==0: # 한번도 방문하지 않은 지점이라면.
            dp[i]=node # 자식 노드 인덱스에 부모 노드 값을 저장한다.
            DFS(i) # 트리의 자식 노드부터 다시 재귀를 시작한다.


N=int(input())

Tree=[ [] for _ in range(N+1) ]

for i in range(N-1):
    a,b=map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

dp=[0]*(N+1)

"""
[ [1,2,3] , [4,5,6] , [7,8,9] ] 

"""

DFS(1)

for i in range(2,len(dp)):
    print(dp[i] , end="\n")