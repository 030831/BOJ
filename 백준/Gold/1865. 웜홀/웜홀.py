import sys

input = sys.stdin.readline

INF = int(1e9)

def Bellman_Ford():
    dp = [INF] * (N + 1)
    dp[1]=0
    for i in range(N):
        for j in range(len(graph)):

            node = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]

            if dp[node] + cost < dp[next_node]:
                dp[next_node] = dp[node] + cost

                if i==N-1:
                    return "YES"

    return "NO"




for i in range(int(input())):
    N, M, W = map(int, input().split())

    graph = []
    for j in range(M):
        a, b, c = map(int, input().split())
        graph.append((a, b, c))
        graph.append((b, a, c))  # 도로는 양방향

    for j in range(W):
        a, b, c = map(int, input().split())
        graph.append((a, b, -c))  # 웜홀은 단방향


    print( Bellman_Ford() )
