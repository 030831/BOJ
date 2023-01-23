def solution(s):
    answer = True
    
    stack=[]
    
    for i in s:
        if i=="(":
            stack.append("(")
        elif i==")":
            try:
                stack.pop()
            except:
                answer=False
    
    if stack:
        answer=False

    return answer