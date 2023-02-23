import sys
input=sys.stdin.readline
from collections import deque

def init(node , start , end):

    if (start==end):
        tree[node] =  L[start]
        return

    init(node*2 , start , (start+end)//2)
    init(node*2+1 , (start+end)//2+1 , end)

    tree[node] = tree[node*2]+tree[node*2+1]

def update(node , start , end , index , value):

    if (index<start or index>end):
        return

    if (start==end):
        tree[node] = value
        return

    update(node*2 , start , (start+end)//2 , index , value)
    update(node*2+1, (start+end)//2+1 , end , index , value)
    tree[node] = tree[node*2]+tree[node*2+1]

def solve(node , start , end , left , right):

    if (left>end or right<start):
        return 0

    if (left<=start and right>=end):
        return tree[node]

    return solve(node*2 , start , (start+end)//2 , left , right) + solve(node*2+1 , (start+end)//2+1 , end , left , right)

N=int(input())
L=list(map(int,input().split()))
tree=[0]*(4*N)

M=int(input())
Change=deque() ; Query=[] ; Query_dict={} ; Query_copy=[]

for i in range(M):
    P=list(map(int,input().split()))

    if P[0]==1:
        Change.append((P[1] , P[2]))
    else:
        Query.append((P[1] , P[2] , P[3]))
        Query_copy.append((P[1] , P[2] , P[3]))

Query_copy.sort(key=lambda x:x[0])

init(1,0,N-1) #초기값 할당

check = 0
for i in range(len(Query_copy)):

    if check == Query_copy[i][0]:
        Query_dict[(Query_copy[i][0] , Query_copy[i][1] , Query_copy[i][2])] = solve(1,0,N-1 ,Query_copy[i][1]-1 , Query_copy[i][2]-1)
    else:
        while check!=Query_copy[i][0]:
            check+=1
            update(1,0,N-1 , Change[0][0]-1, Change[0][1])
            Change.popleft()
        Query_dict[(Query_copy[i][0], Query_copy[i][1], Query_copy[i][2])] = solve(1, 0, N - 1,Query_copy[i][1] - 1,Query_copy[i][2] - 1)

for i in range(len(Query_copy)):
    print(Query_dict[(Query[i][0] , Query[i][1] ,Query[i][2])])
