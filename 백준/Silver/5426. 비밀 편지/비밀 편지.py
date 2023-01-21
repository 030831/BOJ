for i in range(int(input())):
    letter=input()

    graph=[ [] for _ in range(int(len(letter)**0.5))]

    index=0
    for j in range(int(len(letter)**0.5)):
        for k in range(int(len(letter)**0.5)):
            graph[j].append(letter[index])
            index+=1


    for j in range(int(len(letter)**0.5)-1,-1,-1):
        for k in range(int(len(letter)**0.5)):
            print(graph[k][j] , end="")
    print()