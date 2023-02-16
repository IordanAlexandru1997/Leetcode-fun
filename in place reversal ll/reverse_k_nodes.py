class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        curr = self
        while curr:
            print(curr.val, end=" ")
            curr = curr.next


def reverseKGroup(head, k):
    if k == 1 or not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head
    count = 0

    while curr:
        count += 1
        if count % k == 0:
            prev = reverse(prev, curr.next)
            curr = prev.next
        else:
            curr = curr.next

    return dummy.next


def reverse(prev, next):
    last = prev.next
    curr = last.next

    while curr != next:
        last.next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = last.next

    return last


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
# e.next = None
k = 2
print(reverseKGroup(a, k).printList())
