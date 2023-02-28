import sys
input=sys.stdin.readline

L_I=lambda:list(map(int,input().split()))
I_S=lambda:map(int,input().split())
V_L_I=lambda:[ L_I() for _ in range(N) ]
N,M=I_S()
graph=V_L_I()

def A():
    tmp = 0

    for i in range(N):
        for j in range(M):
            if j>=3:
                tmp=max(graph[i][j-3]+graph[i][j-2]+graph[i][j-1]+graph[i][j] , tmp)
            if i>=3:
                tmp=max(graph[i-3][j]+graph[i-2][j]+graph[i-1][j]+graph[i][j] , tmp)

    return tmp

def B():
    tmp=0
    for i in range(N):
        for j in range(M):
            if i>=1 and j>=1:
                tmp=max(graph[i][j]+graph[i-1][j]+graph[i][j-1]+graph[i-1][j-1] , tmp)
    return tmp

def C():

    tmp=0

    for i in range(N):
        for j in range(M):
            if i>=2 and j>=1:
                tmp=max(graph[i][j-1]+graph[i-1][j-1]+graph[i-2][j-1]+graph[i][j]
                        ,graph[i-2][j-1]+graph[i-2][j]+graph[i-1][j]+graph[i][j]
                        ,graph[i-2][j]+graph[i-1][j]+graph[i][j]+graph[i][j-1]
                        ,graph[i-2][j-1]+graph[i-1][j-1]+graph[i][j-1]+graph[i-2][j]
                        ,tmp)
            if i>=1 and j>=2:
                tmp=max(graph[i-1][j]+graph[i][j-2]+graph[i][j-1]+graph[i][j] ,
                        graph[i-1][j-2]+graph[i-1][j-1]+graph[i-1][j]+graph[i][j-2]
                        ,graph[i-1][j-2]+graph[i][j-2]+graph[i][j-1]+graph[i][j]
                        ,graph[i-1][j-2]+graph[i-1][j-1]+graph[i-1][j]+graph[i][j]
                        ,tmp)
    return tmp


def D():
    tmp=0
    for i in range(N):
        for j in range(M):
            if i>=2 and j>=1:
                tmp=max(graph[i-2][j-1]+graph[i-1][j-1]+graph[i-1][j]+graph[i][j]
                        , graph[i-2][j]+graph[i-1][j]+graph[i-1][j-1]+graph[i][j-1]
                        , tmp)
            if i>=1 and j>=2:
                tmp=max(graph[i-1][j-1]+graph[i-1][j]+graph[i][j-2]+graph[i][j-1]
                        ,graph[i-1][j-2]+graph[i-1][j-1]+graph[i][j-1]+graph[i][j]
                        ,tmp)
    return tmp

def E():
    tmp=0
    for i in range(N):
        for j in range(M):
            if i>=1 and j>=2:
                tmp=max(graph[i-1][j-1]+graph[i][j-2]+graph[i][j-1]+graph[i][j]
                        ,graph[i-1][j-2]+graph[i-1][j-1]+graph[i-1][j]+graph[i][j-1]
                        ,tmp)
            if i>=2 and j>=1:
                tmp=max(graph[i-2][j-1]+graph[i-1][j-1]+graph[i][j-1]+graph[i-1][j]
                        ,graph[i-2][j]+graph[i-1][j]+graph[i][j]+graph[i-1][j-1]
                        ,tmp)
    return tmp

print(max(A() , B() , C() , D() , E() ))