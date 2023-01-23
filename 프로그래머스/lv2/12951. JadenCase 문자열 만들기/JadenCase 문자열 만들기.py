def solution(s):

#3people unFollowed me

    s=s.lower()
    String=""
    for i in range(len(s)):
        if i==0:
            String+=s[i].upper()
        elif i!=0:
            if "a" <= s[i] <= "z" and s[i-1]==" ":
                String+=s[i].upper()
            else:
                String+=s[i]
        else:
            String+=s[i]

    return String

