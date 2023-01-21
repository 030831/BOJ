from collections import defaultdict
while True:
    try:
        a=input()
        b=input()

        L1=defaultdict(int)
        L2=defaultdict(int)

        for i in a:
            L1[i]+=1
        for i in b:
            L2[i]+=1

        L=[]

        for i in L1:
            if i in L2:
                L.append(i*min(L1[i] , L2[i]))
                
        L.sort()
        
        for i in L:
            print(i ,end="")
        print()
    except:
        break