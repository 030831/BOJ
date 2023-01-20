graph=[ list(map(str,input().split())) for i in range(5)]


check=set()
dx=[0,0,1,-1]
dy=[-1,1,0,0]

def DFS(x,y,number):
    if len(number)==6:
        if number not in check:
            check.add(number)
        return
    for i in range(4):
        nx=x+dx[i] ; ny=y+dy[i]
        if 0<=nx<5 and 0<=ny<5:
            DFS(nx,ny,number+graph[nx][ny])

for i in range(5):
    for j in range(5):
        DFS(i,j ,graph[i][j])

print(len(check))