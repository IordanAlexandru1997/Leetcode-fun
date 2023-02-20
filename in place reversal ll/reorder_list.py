class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        curr = self
        while curr:
            print(curr.val, end=" ")
            curr = curr.next


def reorder_list(head):

    curr = head
    cnt = 0
    while curr:
        cnt += 1
        curr = curr.next
    if cnt == 0 or cnt == 1:
        return head
    prev = LinkedListNode(0)
    # dummy = LinkedListNode(0)
    dummy = prev
    prev.next = head

    last = prev.next
    curr = last.next

    mid = LinkedListNode(0)
    flag = False
    # reversing second half of linked list
    for i in range(cnt):
        if i > cnt / 2 and curr:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        elif curr and i < cnt:
            prev = prev.next
            last = last.next
            curr = curr.next
    # print(prev.next.val)
    t = dummy.next
    curr = prev.next
    while curr and t:
        prev.next = curr.next
        curr.next = t.next
        t.next = curr
        t = t.next.next
        curr = prev.next

    return dummy.next


a = LinkedListNode(10)
b = LinkedListNode(20)
c = LinkedListNode(-22)
d = LinkedListNode(21)
# e = LinkedListNode(-12)
# f = LinkedListNode(-1)
# g = LinkedListNode(10)
# h = LinkedListNode(12)

# a = LinkedListNode(1)
# b = LinkedListNode(2)
# c = LinkedListNode(3)
# d = LinkedListNode(4)
# e = LinkedListNode(5)
# f = LinkedListNode(6)
# g = LinkedListNode(7)
# h = LinkedListNode(8)

a.next = b
b.next = c
c.next = d
# d.next = e
# e.next = f
# f.next = g
# g.next = h

print(reorder_list(a).printList())
