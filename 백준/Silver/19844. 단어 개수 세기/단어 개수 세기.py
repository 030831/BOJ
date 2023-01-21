import re

a=input()
String=list(re.split('[-| ]' , a))


P=["c'" , "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'" ]
Q=["a" , "e" , "i" , "o" , "u" , "h"]
R=[]

for i in range(len(P)):
    for j in range(len(Q)):
        R.append(P[i]+Q[j])
total=0

for i in range(len(String)):
    for j in range(len(R)):
        if R[j] in String[i]:
            if R[j]==String[i][:len(R[j])]:
                total+=1
                break
print(len(String) + total )