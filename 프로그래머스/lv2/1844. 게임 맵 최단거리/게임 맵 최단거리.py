from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def BFS(N,M,graph):
    deq=deque()
    deq.append([0,0])
    visit=[ [False]*M for _ in range(N)]
    
    visit[0][0]=True
    
    
    while deq:
        x,y=deq.popleft()
        
        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1 and not visit[nx][ny]:
                visit[nx][ny]=visit[x][y]+1
                deq.append([nx,ny])
    return visit[N-1][M-1]
    
def solution(maps):
    N=len(maps)
    M=len(maps[0])
    
    Answer = BFS(N,M,maps)
    
    if Answer==0:
        return -1
    else:
        return Answer    
    