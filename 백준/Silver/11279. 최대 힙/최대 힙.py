import heapq,sys
input=sys.stdin.readline

N=int(input())

heap=[]


for i in range(N):

    K=int(input())

    if K!=0:
        heapq.heappush(heap , (-K,K))

    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
