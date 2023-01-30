"""
DFS - 바이러스
"""

import sys
input=sys.stdin.readline

def DFS(node):
    global count

    visit[node]=True # 재방문을 하지 않는다.

    for i in graph[node]:
        if not visit[i]: # 방문하지 않는 지점이 있으면 , 재귀로 탐색한다.
            count+=1 # 1과 연결된 지점이 존재하므로 경우의 수를 1 추가한다.
            DFS(i)


N=int(input())
K=int(input())

graph=[ [] for _ in range(N+1) ]
visit=[False]*(N+1)

for i in range(K):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a) # 그래프는 양방향.

count=0
DFS(1)

print(count)