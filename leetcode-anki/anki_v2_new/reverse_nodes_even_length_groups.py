def reverseEvenLengthGroups(head):
    l = 2
    
    prev = head 
    curr = head.next
    last = curr.next

    cnt = 0
    while curr:
        cnt += 1
        curr = curr.next

    for i in range(cnt):
        if l % 2 == 0:
            