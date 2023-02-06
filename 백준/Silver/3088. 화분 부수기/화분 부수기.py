import sys
input=sys.stdin.readline

N=int(input())
graph=[ list(map(int,input().split())) for _ in range(N) ]
total=0

check=set()

for i in range(N):
    if graph[i][0] in check or graph[i][1] in check or graph[i][2] in check:
        pass
    else:
        total+=1
    check.add(graph[i][0])
    check.add(graph[i][1])
    check.add(graph[i][2])


print(total)