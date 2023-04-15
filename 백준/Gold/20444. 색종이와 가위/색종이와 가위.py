N,K=map(int,input().split())
"""2번 가위질
2 , 4
3번 가위질
4 , 6
4번 가위질
5, 8 , 9
5번 가위질
6 , 10 , 12 
6번 가위질
7, 12 , 16  
7번 가위질
8 , 14 , 18 , 20
(7+1)*(0+1)=8
(6+1)*(1+1)=14
(5+1)*(2+1)=18
(4+1)*(3+1)=20
0부터 7//2까지
"""
start=0 ; end=N
while start<=end:
    mid=(start+end)//2
    if (mid+1)*( (N-mid) +1 )>K:
        start=mid+1
    elif (mid+1)*( (N-mid) +1 ) <K:
        end=mid-1
    elif (mid+1)*( (N-mid) +1 ) == K:
        print("YES")
        exit(0)
print("NO")