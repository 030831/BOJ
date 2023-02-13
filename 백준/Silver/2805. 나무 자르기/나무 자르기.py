import sys

input=sys.stdin.readline

N, M = map(int, input().split())

tree = list(map(int, input().split()))

tree.sort()

start, end =0, max(tree)

while(start <= end):

  log = 0

  mid = (start+end)//2

  for i in tree:

    if i >= mid:

            log += i - mid

  

  # 나무길이가 요구사항보다 클 때

  if log >= M:

    start = mid+1

  # 나무길이가 요구사항이랑 같거나 작을 때

  else :

    end = mid-1

print(end)