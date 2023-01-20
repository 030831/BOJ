from collections import deque

def BFS():

    while deq:

        x,y=deq.popleft()

        if x==B:
            return y

        if x*2<=B:
            deq.append([ x*2 , y+1])
        if x*10+1<=B:
            deq.append( [ x*10+1 , y+1] )

    return -1

A,B=map(int,input().split())

deq=deque()
deq.append([A,1])

print( BFS() )
