import sys
input=sys.stdin.readline

LMI=lambda:list(map(int,input().split()))
MI=lambda:map(int,input().split())
G=lambda x:[ LMI() for _ in range(x) ]
V=lambda x,y:[ [False]*y for _ in range(x) ]

N,L=MI()
graph=G(N)
total = 0

def Solve(graph):
    for i in range(1,N):
        if abs(graph[i]-graph[i-1])>1:
            return False
        if graph[i-1]>graph[i]:
            for j in range(L):
                if i+j>=N or graph[i]!=graph[i+j] or visit[i+j]:
                    return False
                if graph[i]==graph[i+j]:
                    visit[i+j]=True
        elif graph[i-1]<graph[i]:
            for j in range(L):
                if i-j-1<0 or graph[i-1]!=graph[i-j-1] or visit[i-j-1]:
                    return False
                if graph[i-1]==graph[i-j-1]:
                    visit[i-j-1]=True

    return True

for i in range(N):
    visit=[False]*N
    if Solve([graph[i][j] for j in range(N)]):
        total+=1

for j in range(N):
    visit=[False]*N
    if Solve([graph[i][j] for i in range(N)]):
        total+=1
print(total)