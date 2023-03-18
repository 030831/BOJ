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


def removeBlue(idx):
    for j in range(idx,0,-1):
        for i in range(4):
            blue[i][j]=blue[i][j-1]
    for i in range(4):
        blue[i][0] = 0

def checkBlue():
    global ans

    for i in range(2,6):
        count = 0
        for j in range(4):
            if blue[j][i]:
                count+=1
        if count==4:
            ans+=1
            removeBlue(i)

def goToBlue(t,x):
    global blue
    y=1

    if t==1 or t==2:
        while True:
            if y+1>5 or blue[x][y+1]:
                blue[x][y]=1
                if t==2:
                    blue[x][y-1]=1
                break
            y+=1
    else:
        while True:
            if y+1>5 or blue[x][y+1] or blue[x+1][y+1]:
                blue[x][y],blue[x+1][y]=1,1
                break
            y+=1


    checkBlue()

    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                removeBlue(5)
                break

def removeGreen(idx):
    for i in range(idx,0,-1):
        for j in range(4):
            green[i][j]=green[i-1][j]
    for j in range(4):
        green[0][j]=0
def checkGreen():
    global ans

    for i in range(2,6):
        count = 0
        for j in range(4):
            if green[i][j]:
                count+=1
        if count==4:
            ans+=1
            removeGreen(i)
def goToGreen(t,y):
    global green

    x=1

    if t==1 or t==3:
        while True:
            if x+1>5 or green[x+1][y]:
                green[x][y]=1
                if t==3:
                    green[x-1][y]=1
                break
            x+=1

    else:
        while True:
            if x+1>5 or green[x+1][y] or green[x+1][y+1]:
                green[x][y],green[x][y+1]= 1, 1
                break
            x+=1

    checkGreen()
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                removeGreen(5)
                break

N=I()
blue = [ [0]*6 for _ in range(4) ]
green= [ [0]*4 for _ in range(6) ]

ans = 0 ; blockCount=0
for i in range(N):
    t,x,y=MI()
    goToGreen(t,y)
    goToBlue(t,x)

for i in range(4):
    for j in range(2,6):
        blockCount+=blue[i][j]+green[j][i]

print(ans , blockCount , sep='\n')
