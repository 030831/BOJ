import sys,math
input=sys.stdin.readline

def init(L , tree , node , start , end ): # 트리 기초 구성

    if start==end:
        tree[node]=L[start]

    else:

        init(L,tree,node*2 , start , (start+end)//2)
        init(L , tree, node*2+1 , (start+end)//2 +1 , end)

        tree[node]=(tree[node*2]*tree[node*2+1])%1000000007 # 구간 곱


def update(L , tree , node , start , end , index , value): # 변경

    if index<start or index>end:
        return

    if start==end: #리프 노드에 도착했다면.
        L[index]=value
        tree[node]=value
        return

    update(L,tree, node*2 , start , (start+end)//2 , index , value)
    update(L,tree,node*2+1 , (start+end)//2+1 , end , index , value)

    tree[node] = (tree[node * 2] * tree[node * 2 + 1])%1000000007  # 구간 곱


def query(tree, node , start  , end , left , right): # 구간 곱

    if left>end or right<start:
        return 1

    if left<=start and right>=end:  # 더 크게 포함하고 있다면
        return tree[node]%1000000007

    leftmin=query(tree,node*2,start, (start+end)//2 , left , right)%1000000007
    rightmin=query(tree, node*2+1 ,  (start+end)//2+1 , end , left , right)%1000000007

    return leftmin*rightmin%1000000007

N,M,K=map(int,input().split())  #N은 수의 개수 M은 수의 변경 개수 , K 는 구간 곱의횟수

L=[ int(input()) for _ in range(N) ]
height=math.ceil(math.log2(N))
tree_size=1<<(height+1)
tree=[0]*(tree_size+1)

init(L,tree, 1 , 0 , N-1 )

for i in range(M+K):

    a,b,c=map(int,input().split())

    if a==1:
        index,value=b-1,c
        update(L,tree, 1, 0 , N-1 , index , value)
    else:
        left,right=b-1,c-1
        print( query(tree, 1 , 0 , N-1 , left, right )%1000000007)