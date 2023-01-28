import sys
sys.setrecursionlimit(10**5)

def preorder(node):

    if node!=".":
        print(node , end="")
        preorder(Tree[node][0])
        preorder(Tree[node][1])

def inorder(node):
    if node!=".":
        inorder(Tree[node][0])
        print(node ,end="")
        inorder(Tree[node][1])

def postorder(node):
    if node!=".":
        postorder(Tree[node][0])
        postorder(Tree[node][1])
        print(node , end="")


N=int(input())
Tree={}

for i in range(N):
    parent,left_node,right_node=input().split()

    Tree[parent]=[left_node,right_node]


preorder('A')
print()
inorder('A')
print()
postorder('A')