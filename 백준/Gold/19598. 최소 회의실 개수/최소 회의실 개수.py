import sys,heapq
input=sys.stdin.readline

N=int(input())

L=[ list(map(int,input().split())) for _ in range(N) ]

L.sort()
heap=[] ; heapq.heappush(heap , L[0][1])
Answer = 1
for i in range(1,N):
    if L[i][0]>=heap[0]: # 시작시간이 힙의 최소값 보다 크다면
        heapq.heappop(heap)
    else:
        Answer+=1
    heapq.heappush(heap,L[i][1])
print(Answer)