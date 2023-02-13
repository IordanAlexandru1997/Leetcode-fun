def is_palindrome(s):
    def verify(s, left, right, deleted):
        while left < right:
            if s[left] != s[right]:
                if deleted:
                    return False
                else:
                    return verify(s, left + 1, right, True) or verify(
                        s, left, right - 1, True
                    )
            else:
                left += 1
                right -= 1
        return True

    return verify(s, 0, len(s) - 1, False)


s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(is_palindrome(s))
