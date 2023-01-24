def solution(s):
    total = 0
    a = 0
    while True:
        if s == "1":
            break

        total += s.count("0")
        s = s.replace("0", "")

        s = bin(len(s))
        s = str(s)

        s=s.replace("0b" , "")
        a += 1
    return [a, total]

