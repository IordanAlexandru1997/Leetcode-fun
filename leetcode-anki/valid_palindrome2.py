def solution(s):
    start, end = 0, len(s) - 1
    cnt = 1
    while start < end and cnt <= 2:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            if cnt > 2:
                return False
            if s[start + 1] == s[end]:
                start += 1
            elif s[end - 1] == s[start]:
                end -= 1
            else:
                return False
            cnt += 1
    return True


def solution2(s):
    def verify(s, start, end, deleted):
        while start < end:
            if s[start] != s[end]:
                if deleted:
                    return False
                return verify(s, start + 1, end, True) or verify(
                    s, start, end - 1, True
                )
            return True

    return verify(s, 0, len(s) - 1, False)


def solution3(s):
    def verify(s, start, end, deleted):
        while start < end:
            if s[start] != s[end]:
                if deleted:
                    return False
                return verify(s, start + 1, end, True) or verify(
                    s, start, end - 1, True
                )
            start += 1
            end -= 1
        return True

    return verify(s, 0, len(s) - 1, False)


s = "abca"
# s = "abc"
print(solution3(s))
