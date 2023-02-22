def reverse_even_length_groups(head):
    l = 2
    prev = head
    while prev.next:
        n = 0
        node = prev
        for i in range(l):
            if not node.next:
                break

            n += 1
            node = node.next

        if n % 2 == 1:
            prev = node
        else:
            reverse = node.next
            curr = prev.next
            for j in range(n):
                curr_next = curr.next
                curr.next = reverse
                reverse = curr
                curr = curr_next
            prev_next = prev.next
            prev.next = node
            prev = prev_next
        l += 1
    return head
