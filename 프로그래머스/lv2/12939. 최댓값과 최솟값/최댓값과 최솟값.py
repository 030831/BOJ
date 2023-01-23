def solution(s):

    L=list(map(int,s.split()))
    
    return "%d %d"%( min(L),max(L) )