a=int(input())
b=1
for i in range(1,a+1):
    b=b*i
b=str(b)
b=list(b)
count=0
for i in range(-1,-len(b)+1,-1):
    if b[i]=='0':
        count+=1
    elif b[i]!='0':
        break
print(count)