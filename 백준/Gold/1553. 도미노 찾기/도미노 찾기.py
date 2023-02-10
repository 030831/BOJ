graph = [list(map(int, list(input()))) for _ in range(8)]
visit = [[False] * 7 for _ in range(8)]
D = [[False] * 7 for _ in range(7)]


def Back_Tracking(x,y):
    if x==8:
        return 1 # 탐색완료
    count = 0
    nx,ny=x,y+1 # 오른쪽이동

    if ny==7: # 오른쪽 끝이라면
        nx,ny=x+1,0 # 가장 왼쪽  , 밑으로 이동

    if visit[x][y]:
        return Back_Tracking(nx,ny) # 현재 칸이 방문한 칸이라면 다음 칸으로 이동한다.
    else:
        visit[x][y]=True
        now = graph[x][y]
        for dx,dy in ((0,1) ,(1,0)): #오른쪽 , 아래
            mx,my=x+dx,y+dy
            if 0<=mx<8 and 0<=my<7:
                next=graph[mx][my]
                if not visit[mx][my] and not D[now][next]:
                    D[now][next]=D[next][now]=True
                    visit[mx][my]=True

                    count+= Back_Tracking(nx,ny)

                    D[now][next]=D[next][now]=False
                    visit[mx][my]=False
        visit[x][y]=False
        return count


print(Back_Tracking(0,0))