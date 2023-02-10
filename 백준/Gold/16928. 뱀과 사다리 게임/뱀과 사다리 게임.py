from collections import deque


def BFS():

    while deq:
        x,total=deq.popleft()

        if x==100:
            return total

        for i in range(1,7):
            nx=x+i
            if nx<=100 and not visit[nx]:
                check = False
                for j in range(N):
                    if N_list[j][0] == nx:
                        deq.append([N_list[j][1], total + 1])
                        visit[N_list[j][1]] = True
                        check=True
                for j in range(M):
                    if M_list[j][0] == nx:
                        deq.append([M_list[j][1], total + 1])
                        visit[M_list[j][1]] = True
                        check=True
                if not check:
                    visit[nx]=True
                    deq.append([nx,total+1])


N,M=map(int,input().split())

deq=deque() ;  deq.append((1,0))

visit=[False]*101
N_list=[ list(map(int,input().split())) for _ in range(N) ]
M_list=[ list(map(int,input().split())) for _ in range(M) ]

print( BFS() )