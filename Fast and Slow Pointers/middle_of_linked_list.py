def get_middle_node(head):
    slow, fast = head, head
    while fast.next:
        slow = slow.next
        if fast.next.next:
            fast = fast.next.next
        else:
            return slow
    return slow
