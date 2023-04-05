import sys
input=sys.stdin.readline

def init(node,start,end):

    if start==end:
        tree[node]=0

    else:
        init(node*2 , start , (start+end)//2)
        init(node*2+1,  (start+end)//2+1 , end)

        tree[node]=tree[node*2]+tree[node*2+1]


def update(node,start,end,value,index):

    if index<start or index>end: #범위 밖이라면
        return

    if start==end:
        tree[node]=value
        return

    update(node*2 , start , (start+end)//2  ,value , index)
    update(node*2+1 , (start+end)//2+1 , end , value , index)

    tree[node]=tree[node*2]+tree[node*2+1]
    return

def query(node,start,end,left,right):

    if left>end or right<start:
        return 0

    if left<=start and right>=end:

        return tree[node]

    return query(node*2,start,(start+end)//2 , left,right) +query(node*2+1, (start+end)//2+1  , end , left , right)


N=int(input())
L=list(map(int,input().split()))
tree=[0]*(4*N)
total=0

L2=[]
init(1, 1, N)

for i in range(N):
    L2.append( (L[i],i+1) )

L2.sort()
for i in range(N):

    Q,index=L2[i]
    total+=query(1,1,N,index+1,N)
    update(1,1,N, 1 , index)

print(total)