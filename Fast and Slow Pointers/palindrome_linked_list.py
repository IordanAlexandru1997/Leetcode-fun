def palindrome(head):
    d = {}
    s, f = head, head
    flag = 0
    cnt = 0
    mid = 0
    while s.next:
        if flag == 0:
            d[s.data] = 1 + d.get(s.data, 0)
        else:
            d[s.data] -= 1
        s = s.next
        if f.next.next:
            f = f.next.next
        else:
            mid = cnt
            flag = 1
        cnt += 1
    if cnt % 2 == 0 and all(k == 0 for k, _ in d.items()):
        return True
    elif cnt % 2 == 1 and d.get(mid) == 1:
        return True
    else:
        return False
