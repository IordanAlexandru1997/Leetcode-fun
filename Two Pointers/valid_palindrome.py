def is_palindrome(s):
    ptr1 = 0
    ptr2 = len(s) - 1
    while ptr1 < ptr2:
        if s[ptr1] != s[ptr2]:
            return False
        ptr1 += 1
        ptr2 -= 1
    return True
