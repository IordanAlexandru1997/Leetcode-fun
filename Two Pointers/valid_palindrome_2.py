def is_palindrome(s):
    start = 0
    end = len(s) - 1
    flag = 0
    while start < end and flag < 2:
        if s[start] != s[end]:
            if s[start + 1] == s[end]:
                start += 1
            elif s[end - 1] == s[start]:
                end -= 1
            flag += 1
        start += 1
        end -= 1
    return True if flag < 2 else False


s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(is_palindrome(s))
