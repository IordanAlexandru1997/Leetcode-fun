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


s = "A man, a plan, a canal: Panama"
# s = "race a car"
print(solution(s))
