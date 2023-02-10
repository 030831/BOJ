from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS():
    global visit
    now = 2 ; Baby=[]
    total = 0 ; Answer=[]

    while shark:
        x,y=shark.popleft()



        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N and now>=graph[nx][ny] and not visit[nx][ny]:
                if graph[nx][ny]!=0 and graph[nx][ny]<now: # 먹을수 있다면.
                    Baby.append([nx,ny, visit[x][y]])
                shark.append([nx,ny])
                visit[nx][ny]=visit[x][y]+1

        if not shark:
            if len(Baby)==1:
                if visit[Baby[0][0]][Baby[0][1]] != 1:
                    shark.clear()
                    Answer.append( Baby[0][2] )
                    graph[Baby[0][0]][Baby[0][1]]=0
                    visit = [[0] * N for _ in range(N)]
                    visit[Baby[0][0]][Baby[0][1]]=1
                    shark.append([Baby[0][0],Baby[0][1]])
                    Baby.clear()

                    total+=1

                    if total==now:
                        now+=1 ; total = 0

            elif len(Baby)>1:

                Baby.sort(key=lambda x: x[1])
                Baby.sort(key=lambda x: x[0])
                Baby.sort(key=lambda x: x[2])
                shark.clear()

                for i in range(len(Baby)):

                    if visit[Baby[i][0]][Baby[i][1]]!=1:
                        Answer.append( Baby[0][2] )
                        graph[Baby[i][0]][Baby[i][1]]=0
                        visit = [[0] * N for _ in range(N)]
                        visit[Baby[i][0]][Baby[i][1]]=1
                        shark.append([Baby[i][0],Baby[i][1]])
                        total += 1
                        Baby.clear()

                        if total == now:
                            now += 1 ;total = 0
                        break

    return sum(Answer)



N=int(input())

graph=[list(map(int,input().split())) for _ in range(N) ]
visit = [[0] * N for _ in range(N)]

shark = deque()

for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            shark.append([i,j])
            graph[i][j]=0
            visit[i][j]=1

print( BFS() )