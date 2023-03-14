import sys,math
input=sys.stdin.readline

def init(L,tree,node,start,end): # 세그먼트 트리를 구성한다.

    if start==end: # 리프 노드라면. 즉 구간의 범위가 하나만 존재해서 start 와 end가 값이 같다면.
        tree[node]=L[start]
    else:
        init(L,tree,node*2,start,(start+end)//2) # 왼쪽 자식 노드로 이동한다.
        init(L,tree,node*2+1,(start+end)//2+1 , end) #오른쪽 자식 노드로 이동한다.

        # 0~9 일때 왼쪽은 0~4  , 오른쪽은 5~9로 이동한다.
        tree[node]=tree[node*2]+tree[node*2+1]
        # 부모자식은 두개의 자식의 범위의 합이므로 두 자식의 범위의 합을 더해준다.

def update(L,tree,node,start,end,index,value): #업데이트.

    if index<start or index>end: # 범위에 벗어난다면.
        return #종료한다.

    if start==end: #리프노드에 도착했다면
        L[index]=value
        tree[node]=value
        return

    update(L,tree,node*2,start,(start+end)//2 ,index,value)
    update(L,tree,node*2+1 , (start+end)//2+1 , end, index, value)

    tree[node]=tree[node*2]+tree[node*2+1]

def query(tree,node,start,end,left,right):

    if left>end or right<start: # 범위에 벗어나있다면 , 즉 왼쪽값이 범위의 오른쪽값보다 크거나 또는 오른쪽값이 범위의 왼쪽값보다 작다면.
        return 0 # 0 를 반환한다

    if left<=start and end<=right: #왼쪽값이 범위의 왼쪽값보다 작고 오른쪽값이 범위의 오른쪽값보다 크다면. 즉 더 크게 포함하고 있다면
        return tree[node]

    leftmin=query(tree,node*2,start,(start+end)//2 , left,right)
    rightmin=query(tree,node*2+1,(start+end)//2+1 , end , left , right)

    return leftmin+rightmin # 구간의 합. 왼쪽의 범위의 합과 오른쪽 범위의 합을 더해서 반환한다.

N,M,K=map(int,input().split()) #수의 개수 , 수의 변경이 일어나는 횟수  K 는 구간의 합을 구하는 횟수

L=[int(input()) for _ in range(N) ] #리스트.

height=math.ceil(math.log2(N)) # 트리의 높이. 반올림을 해준다.

tree_size=1<<(height+1) # 크리의 크기. 최대 2^(height+1) 이다.

tree=[0]*(tree_size+1)

init(L, tree, 1, 0 , N-1)
# 리스트 L 값을 가지고 tree , 세그먼트 트리를 설계한다. 노드의 시작번호는 1 이고 범위는 0부터 N-1까지이다.


for i in range(M+K):

    a,b,c=map(int,input().split())

    if a==1: #a 가 1이면 b번째 수를 c로 바꾼다.
        index,value=b,c
        update(L,tree,1,0,N-1,b-1,c) #인덱스는 0부터 시작이기 때문에 b가 아니라 b-1 을 한다.

    else: # a 가 2인 경우에는 b번째 수부터 C번째 수의 합을 구한다.
        left,right=b,c
        print( query(tree,1,0,N-1,left-1,right-1) )
        #tree 에서 1번째 노드번호에서 시작한다. 범위는 0부터 N-1 이고 left-1 에서 right-1 범위의 값의 합을 구한다.


