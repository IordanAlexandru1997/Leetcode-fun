def validPalidrome(s):
    def checker(s, start, end, deleted):
        while start < end:
            if s[start] != s[end]:
                if deleted:
                    return False
                return checker(s, start + 1, end, True) or checker(
                    s, start, end - 1, True
                )
            start += 1
            end -= 1
        return True

    return checker(s, 0, len(s) - 1, False)
