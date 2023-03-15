import sys
input=sys.stdin.readline
from collections import deque
LMI=lambda:list(map(int,input().split()))
LMS=lambda:list(map(str,input().split()))
MI=lambda:map(int,input().split())
I=lambda:int(input())
GI=lambda x:[ LMI() for _ in range(x) ]
GS=lambda x:[ LMS() for _ in range(x) ]
V=lambda x,y:[ [False]*y for _ in range(x) ]



def Get_Bead(graph):
    P=deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j]=='R':
                P.append((i,j,'R'))
            elif graph[i][j]=='B':
                P.append((i,j,'B'))
    return P
def Left(graph):

    P=Get_Bead(graph)

    if len(P)!=2:
        return 0
    check_R = 0
    check_B = 0
    if P[0][1]>P[1][1]: # 더 왼쪽에있는 구슬을 먼저 이동시킨다.
        P[0],P[1]=P[1],P[0]

    new_P = [ i[:] for i in P ]
    graph[P[0][0]][P[0][1]]='.'
    graph[P[1][0]][P[1][1]]='.'

    for i in range(2):
        x,y,color = P.popleft()
        while True:
            if graph[x][y]=='.':
                y-=1
            elif graph[x][y]=='O':
                if color == 'R':
                    check_R = 1
                else:
                    check_B = 1
                break
            else:
                graph[x][y+1]=color
                break

    if check_R == 1 and check_B==0:
        return 1
    elif (graph[new_P[0][0]][new_P[0][1]]==new_P[0][2] and graph[new_P[1][0]][new_P[1][1]]==new_P[1][2]) or check_B == 1:
        return -1
    else:
        return 0
def Right(graph):
    P=Get_Bead(graph)
    if len(P)!=2:
        return 0
    if P[0][1]<P[1][1]: # 더 오른쪽에 있는 구슬을 먼저 이동시킨다.
        P[0],P[1]=P[1],P[0]

    graph[P[0][0]][P[0][1]]='.'
    graph[P[1][0]][P[1][1]]='.'
    new_P = [i[:] for i in P]
    check_R = 0
    check_B = 0
    for i in range(2):
        x,y,color = P.popleft()
        while True:
            if graph[x][y]=='.':
                y+=1
            elif graph[x][y]=='O':
                if color=='R':
                    check_R = 1
                else:
                    check_B = 1
                break
            else:
                graph[x][y-1]=color
                break
    if check_R == 1 and check_B==0:
        return 1
    elif (graph[new_P[0][0]][new_P[0][1]]==new_P[0][2] and graph[new_P[1][0]][new_P[1][1]]==new_P[1][2]) or check_B==1:
        return -1
    else:
        return 0
def Up(graph):

    P = Get_Bead(graph)
    if len(P)!=2:
        return 0
    if P[0][0] > P[1][0]:  # 더 위쪽에 있는 구슬을 먼저 이동시킨다.
        P[0], P[1] = P[1], P[0]
    new_P = [i[:] for i in P]
    graph[P[0][0]][P[0][1]]='.'
    graph[P[1][0]][P[1][1]]='.'

    check_R = 0
    check_B = 0
    for i in range(2):
        x, y, color = P.popleft()
        while True:
            if graph[x][y]=='.':
                x-=1
            elif graph[x][y]=='O':
                if color=='R':
                    check_R = 1
                else:
                    check_B = 1
                break
            else:
                graph[x+1][y]=color
                break
    if check_R == 1 and check_B==0:
        return 1
    elif (graph[new_P[0][0]][new_P[0][1]]==new_P[0][2] and graph[new_P[1][0]][new_P[1][1]]==new_P[1][2]) or check_B==1:
        return -1
    else:
        return 0

def Down(graph):

    P = Get_Bead(graph)
    if len(P)!=2:
        return 0
    if P[0][0] < P[1][0]:  # 더 아래쪽에 있는 구슬을 먼저 이동시킨다.
        P[0], P[1] = P[1], P[0]
    new_P = [i[:] for i in P]
    graph[P[0][0]][P[0][1]]='.'
    graph[P[1][0]][P[1][1]]='.'
    check_R = 0
    check_B = 0
    for i in range(2):
        x, y, color = P.popleft()
        while True:
            if graph[x][y] == '.':
                x+=1
            elif graph[x][y]=='O':
                if color=='R':
                    check_R = 1
                else:
                    check_B = 1
                break
            else:
                graph[x-1][y]=color
                break
    if check_R==1 and check_B==0:
        return 1
    elif (graph[new_P[0][0]][new_P[0][1]]==new_P[0][2] and graph[new_P[1][0]][new_P[1][1]]==new_P[1][2]) or check_B==1:
        return -1
    else:
        return 0


def BackTracking(deep,graph,string):
    global ans,S

    if ans<=deep:
        return

    if deep==11:
        return

    for i in range(4):
        if i==0: # 왼
            new_graph = [ i[:] for i in graph]
            P = Left(new_graph)
            if P==1:
                if ans>=deep:
                    ans = min(ans , deep)
                    S=string+'L'
                return
            elif P==-1:
                continue
            else:
                BackTracking(deep+1,new_graph,string+'L')
        elif i==1: #오
            new_graph = [ i[:] for i in graph]

            P = Right(new_graph)
            if P==1:
                if ans>=deep:
                    ans = min(ans , deep)
                    S=string+'R'
                return
            elif P==-1:
                continue
            else:
                BackTracking(deep+1,new_graph,string+'R')
        elif i==2: #위
            new_graph = [ i[:] for i in graph]

            P = Up(new_graph)
            if P==1:
                if ans>=deep:
                    ans = min(ans , deep)
                    S=string+'U'
                return
            elif P==-1:
                continue
            else:
                BackTracking(deep+1,new_graph,string+'U')
        else: # 아래
            new_graph = [ i[:] for i in graph]

            P = Down(new_graph)
            if P==1:
                if ans>=deep:
                    ans = min(ans , deep)
                    S=string+'D'
                return
            elif P==-1:
                continue
            else:
                BackTracking(deep+1,new_graph,string+'D')

N,M=MI()
graph=[ list(input().rstrip()) for _ in range(N) ]
ans = 11
S = ""
BackTracking(1,graph,"")

if ans==11:
    print(-1)
else:
    print(ans)
    print(S)
