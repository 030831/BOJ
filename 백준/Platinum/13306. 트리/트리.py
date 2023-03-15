import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
parent = [i for i in range(N+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x>y:
        parent[x] = y
    else:
        parent[y] = x

tree =[0]*200001
for i in range(2, N + 1):
    tree[i] = int(input())
query = [list(map(int, input().split())) for _ in range(Q + N - 1)]
ans = []
while query:
    q = query.pop()
    if q[0] == 0:
        node = q[1]  # q[1]과 q[1]의 부모사이 간선생성
        union(node, tree[node])
    else:
        a, b = q[1], q[2]  # a,b사이의 경로 질의
        if find(a) == find(b):
            ans.append("YES")
        else:
            ans.append("NO")
while ans:
    print(ans.pop())