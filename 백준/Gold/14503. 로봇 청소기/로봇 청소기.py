import sys
input=sys.stdin.readline

L_I=lambda:list(map(int,input().split()))
I_S=lambda:map(int,input().split())
V_L_I=lambda:[ L_I() for _ in range(N) ]

def BFS(x,y,d):
    # d 0 : 북 , 1 :  동 , 2: 남 , 3 : 서
    total = 0
    if graph[x][y]==0: total+=1
    visit=[ [0]*M for _ in range(N) ]
    visit[x][y]=1


    while True:
        if d==0: # 북
            if y-1>=0 and graph[x][y-1]==0 and not visit[x][y-1]: #서
                total+=1
                visit[x][y-1]=visit[x][y]+1
                y-=1
                d=3
            elif x+1<N and graph[x+1][y]==0 and not visit[x+1][y]: #남
                total+=1
                visit[x+1][y]=visit[x][y]+1
                x+=1
                d=2
            elif y+1<M and graph[x][y+1]==0 and not visit[x][y+1]: # 동
                total+=1
                visit[x][y+1]=visit[x][y]+1
                y+=1
                d=1
            elif x-1>=0 and graph[x-1][y]==0 and not visit[x-1][y]: #북
                total+=1
                visit[x-1][y]=visit[x][y]+1
                x-=1
            else:
                if x+1<N and graph[x+1][y]==0:
                    visit[x+1][y]=visit[x][y]
                    x+=1
                else:
                    return total

        elif d==1: #동
            if x-1>=0 and graph[x-1][y]==0 and not visit[x-1][y]: # 북
                total+=1
                visit[x-1][y]=visit[x][y]+1
                x-=1
                d=0
            elif y-1>=0 and graph[x][y-1]==0 and not visit[x][y-1]: #서
                total+=1
                visit[x][y-1]=visit[x][y]+1
                y-=1
                d=3
            elif x+1<N and graph[x+1][y]==0 and not visit[x+1][y]:#남
                total+=1
                visit[x+1][y]=visit[x][y]+1
                x+=1
                d=2
            elif y+1<M and graph[x][y+1]==0 and not visit[x][y+1]: #동
                total+=1
                visit[x][y+1]=visit[x][y]+1
                y+=1
            else:
                if y-1>=0 and graph[x][y-1]==0:
                    visit[x][y]=visit[x][y-1]
                    y-=1
                else:
                    return total

        elif d==2: #남
            if y+1<M and graph[x][y+1]==0 and not visit[x][y+1]: #동
                total+=1
                visit[x][y+1]=visit[x][y]+1
                y+=1
                d=1
            elif x-1>=0 and graph[x-1][y]==0 and not visit[x-1][y]:# 북
                total+=1
                visit[x-1][y]=visit[x][y]+1
                x-=1
                d=0
            elif y-1>=0 and graph[x][y-1]==0 and not visit[x][y-1]: # 서
                total+=1
                visit[x][y-1]=visit[x][y]+1
                y-=1
                d=3
            elif x+1<N and graph[x+1][y]==0 and not visit[x+1][y]: #남
                total+=1
                visit[x+1][y]=visit[x][y]+1
                x+=1
            else:
                if x-1>=0 and graph[x-1][y]==0:
                    visit[x-1][y]=visit[x][y]
                    x-=1
                else:
                    return total


        elif d==3: #서
            if x+1<N and graph[x+1][y]==0 and not visit[x+1][y]: # 남
                total+=1
                visit[x+1][y]=visit[x][y]+1
                x+=1
                d=2
            elif y+1<M and graph[x][y+1]==0 and not visit[x][y+1]: #동
                total+=1
                visit[x][y+1]=visit[x][y]+1
                y+=1
                d=1
            elif x-1>=0 and graph[x-1][y]==0 and not visit[x-1][y]: # 북
                total+=1
                visit[x-1][y]=visit[x][y]+1
                x-=1
                d=0
            elif y-1>=0 and graph[x][y-1]==0 and not visit[x][y-1]:#서
                total+=1
                visit[x][y-1]=visit[x][y]+1
                y-=1
            else:
                if y+1<M and graph[x][y+1]==0:
                    visit[x][y+1]=visit[x][y]
                    y+=1
                else:
                    return total



N,M=L_I()
x,y,d=L_I()
graph=V_L_I()

print( BFS(x,y,d) )
