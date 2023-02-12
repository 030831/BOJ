# 7569 토마토

from sys import stdin
from collections import deque

x_size, y_size, z_size = list(map(int, input().split(" ")))
graph = [[list(map(int, stdin.readline().rstrip().split(" "))) for y in range(y_size)] for z in range(z_size)]

delta_list = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for dx, dy, dz in delta_list:
            new_x = x + dx
            new_y = y + dy
            new_z = z + dz
            if new_x < 0 or new_x >= x_size or new_y < 0 or new_y >= y_size or new_z < 0 or new_z >= z_size:
                continue
            if graph[new_z][new_y][new_x] == 0:
                graph[new_z][new_y][new_x] = graph[z][y][x] + 1
                queue.append((new_x, new_y, new_z))
    return graph

queue = deque()
for x in range(x_size):
    for y in range(y_size):
        for z in range(z_size):
            if graph[z][y][x] == 1:
                queue.append([x,y,z])
bfs()

def check_unripe_tomato() -> int:
    max_temp = 0
    for x in range(x_size):
        for y in range(y_size):
            for z in range(z_size):
                if not graph[z][y][x]:
                    return -1
                max_temp = max(graph[z][y][x]-1,max_temp)
    return max_temp

print(check_unripe_tomato())