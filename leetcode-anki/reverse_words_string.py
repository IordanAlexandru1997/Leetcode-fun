def solution1(s):
    return " ".join(s.split()[::-1])


s = "the sky is blue"
s = "  hello  world"
print(solution1(s))
