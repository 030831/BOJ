import sys,heapq
input=sys.stdin.readline
INF=int(1e9)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def Dijkstra():

    dp=[ [INF]*(N+1) for _ in range(N+1) ]

    heap=[] ; heapq.heappush(heap,(0 , 0 , 0 , 0))

    while heap:

        value,x,y,total=heapq.heappop(heap)

        if x==N-1 and y==N-1:
            return total
        if dp[x][y]<value:
            continue
        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:

                if abs(graph[x][y]-graph[nx][ny])<dp[nx][ny]: #다음으로 이동할 거리가 현재까지 이동한 거리보다 작다면.
                    dp[nx][ny]=abs(graph[x][y]-graph[nx][ny])
                    heapq.heappush(heap,(abs(graph[x][y]-graph[nx][ny]) , nx , ny , max(total ,dp[nx][ny])))


N=int(input())
graph=[ list(map(int,input().split())) for _ in range(N) ]

print( Dijkstra() )