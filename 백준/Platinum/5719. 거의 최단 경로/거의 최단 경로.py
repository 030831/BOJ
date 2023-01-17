import sys,heapq
input=sys.stdin.readline
from collections import deque
INF=float('inf')

def Dijkstra(start,end, graph):

    heap=[] ; heapq.heappush(heap , (0,start))
    dp=[INF]*N ; dp[start]=0 ; visit=[False]*N

    while heap:
        value,node=heapq.heappop(heap)

        if visit[node]:
            continue

        visit[node]=True

        if dp[node]<value:
            continue

        if node==end:
            return dp

        for next_value,next_node in graph[node]:
            next_value+=value

            if next_value<dp[next_node] and graph_check[node][next_node]:
                dp[next_node]=next_value
                heapq.heappush(heap , (next_value , next_node))



def BFS():

    deq=deque() ; deq.append((0,D))

    while deq:

        value,node=deq.popleft()

        for next_value,next_node in graph_reverse[node]:

            if value+next_value+Short[next_node]==Short[D]:
                if graph_check[next_node][node]:
                    graph_check[next_node][node]=False
                    deq.append((value+next_value,next_node))
while True:

    N,M=map(int,input().split())

    if [N,M]==[0,0]:
        break

    S,D=map(int,input().split())

    graph=[ [] for _ in range(N) ]
    graph_reverse=[ [] for _ in range(N) ]
    graph_check = [ [False]*N for _ in range(N)]


    for i in range(M):
        a,b,c=map(int,input().split())
        graph[a].append((c,b))
        graph_reverse[b].append((c,a))
        graph_check[a][b]=True

    First_check=Dijkstra(S,D,graph)

    if First_check==None:
        print(-1)
        continue

    Short=First_check

    BFS()

    Answer=Dijkstra(S,D,graph)
    if Answer==None:
        print(-1)
    else:
        print(Answer[D])
