def solution(s):
    res = ""
    for c in s:
        if c.isalnum():
            res += c.lower()
    start = 0
    end = len(res) - 1
    while start < end:
        if res[start] != res[end]:
            return False
        else:
            start += 1
            end -= 1
    return True


def solution2(s):
    rez = []
    for c in s:
        if c.isalnum():
            rez.append(c.lower())
    return True if "".join(rez[::-1]) == "".join(rez) else False


s = "A man, a plan, a canal: Panama"
# s = "race a car"
print(solution2(s))
