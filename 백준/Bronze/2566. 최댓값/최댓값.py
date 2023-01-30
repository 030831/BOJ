L=[]
M=-1
graph=[ list(map(int,input().split())) for _ in range(9) ]

for i in range(9):
    for j in range(9):
        if M<graph[i][j]:
            M=graph[i][j]
            L=[i+1,j+1]
print(M)
print(*L)