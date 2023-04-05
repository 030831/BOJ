import sys
input=sys.stdin.readline

def update(idx, val):
    while idx <= N:
        tree[idx] += val
        idx += (idx & -idx)

def query(idx):
    ret = 0
    while idx > 0:
        ret += tree[idx]
        idx -= (idx & -idx)
    return ret

N=int(input())
L=list(map(int,input().split()))
total=0

L2 = [(L[i], i+1) for i in range(N)]
L2.sort(key=lambda x: x[0])

tree=[0]*(N+1)

for i in range(N):
    Q, index = L2[i]
    total += i - query(index)
    update(index, 1)

print(total)
