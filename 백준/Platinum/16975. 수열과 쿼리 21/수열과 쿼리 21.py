import sys,math
input=sys.stdin.readline

def init(node,start,end):

    if start==end:
        tree[node]=L[start]
        return

    init(node*2 , start, (start+end)//2)
    init(node*2+1 , (start+end)//2+1 , end)



def update(node, start , end , left , right , value):

    if left>end or right<start:
        return

    if left<=start and right>=end:

        tree[node]+=value
        return

    update(node*2 , start , (start+end)//2 , left , right , value)
    update(node*2+1 , (start+end)//2+1 , end , left , right , value)


def query(node , start , end , index , value):

    if index>end or index<start:
        return 0

    value+=tree[node]

    if start==end:
        return value #tree[node] 가 아니라 value 를 return 해야한다.

    return query(node*2 , start , (start+end)//2 , index , value) + query(node*2+1 ,(start+end)//2+1,  end, index , value)

N=int(input())
L=list(map(int,input().split()))
height=math.ceil(math.log2(N))
tree_size=1<<(height+1)
tree=[0]*(tree_size+1)

init(1,0,N-1)
for i in range(int(input())):

    M=list(map(int,input().split()))

    if M[0]==1:
        update(1, 0 , N-1 , M[1]-1 , M[2]-1 , M[3])
    else:
        print( query(1,0,N-1,M[1]-1 , 0) )