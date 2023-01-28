"""
우선순위 큐 - 최소힙

매 순간마다의 최소값과 원소삽입을 O(log N) 의 시간복잡도로 해결이 가능하다.
"""
import heapq
import sys
input=sys.stdin.readline


N=int(input())

heap=[]

for i in range(N):

    K=int(input())

    if K==0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap,K)
