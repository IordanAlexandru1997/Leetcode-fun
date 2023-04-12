def hasCycle(head):
    s = head
    f = head
    while f and f.next:
        s = s.next
        f = f.next.next
        if f == s:
            return False
    return True
