import sys
input=sys.stdin.readline

LMI=lambda:list(map(int,input().split()))
MI=lambda:map(int,input().split())
G=lambda x:[ LMI() for _ in range(x) ]
V=lambda x,y:[ [False]*y for _ in range(x) ]

graph=[ [0]*101 for _ in range(101) ]

dx=[0,-1,0,1]
dy=[1,0,-1,0]
direction=[ [(0,1) , (-1,0)] , [(-1,0) , (0,-1)] , [(0,-1) , (1,0)] , [(1,0) , (0,1)] ]
N=int(input())
L=[]
for i in range(N):
    y,x,d,g=MI() #입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다.
    if g==0:
        graph[x][y]=graph[x+dx[d]][y+dy[d]]=1
    else:
        Q=[]
        while g:
            if not Q:
                graph[x][y]=1
                for j in range(2):
                    x+=direction[d][j][0] ; y+=direction[d][j][1]
                    graph[x][y]=1

                if d==0:
                    Q.append([3,1]) # 두번재 값인 0 은 정방향 , 1은 역방향.
                else:
                    Q.append([d-1,1])
                g-=1
            else:
                P=[]

                for j in range(1,len(Q)+1):
                    d=Q[-j][0]
                    if Q[-j][1]==0: # 정방향이라면.
                        if d==0:
                            P.append([3,1])
                        else:
                            P.append([d-1,1])
                        for k in range(2):
                            x+=direction[d][k][0] ; y+=direction[d][k][1]
                            graph[x][y]=1
                    else: # 역방향이라면
                        if d == 0:
                            P.append([3, 0])
                        else:
                            P.append([d - 1, 0])
                        for k in range(-1,-3,-1):
                            x -= direction[d][k][0] ; y -= direction[d][k][1]
                            graph[x][y] = 1
                for a,b in P:
                    Q.append([a,b])
                g-=1


total = 0
for i in range(1,101):
    for j in range(1,101):
        if [graph[i-1][j-1],graph[i-1][j],graph[i][j-1],graph[i][j]]==[1,1,1,1]:
            total+=1
print(total)