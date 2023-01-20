import sys
input=sys.stdin.readline
from collections import deque

for i in range(int(input())):

    N=int(input())
    L=list(input().split())

    deq=deque()

    for j in range(len(L)):
        if not deq:
            deq.append(L[j])
        else:
            if ord(L[j])<=ord(deq[0]):
                deq.appendleft(L[j])

            else:
                deq.append(L[j])


    for j in deq:
        print(j , end="")
    print()