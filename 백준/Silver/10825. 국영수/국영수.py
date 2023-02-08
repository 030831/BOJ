import sys
input=sys.stdin.readline

N=int(input())

graph=[ list(input().split()) for _ in range(N) ]


graph.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(graph[i][0])