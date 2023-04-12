def reverseEvenLengthGroups(head):
    prev = head
    node = prev
    group_size = 2
    while prev:
        node_count = 0
        for i in range(group_size):
            if node.next:
                node_count += 1
                node = node.next
            else:
                break
        if node_count % 2 == 1:
            node = prev
        else:
            last = node.next
            curr = prev.next
            for i in range(node_count):
                curr_next = curr.next
                curr.next = last
                last = curr
