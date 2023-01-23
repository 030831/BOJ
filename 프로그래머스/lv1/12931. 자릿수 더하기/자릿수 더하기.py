def solution(n):

    a=0
    
    for i in range(len(str(n))):
        a+=int(str(n)[i])
    
    return a