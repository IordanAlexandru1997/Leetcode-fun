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
        print(last.val)

    return last


def swap_pairs(head):
    pp = ListNode(0)
    pp.next = head
    p = head
    curr = p.next
    dummy = head.next
    while p and curr:
        p.next = curr.next
        curr.next = p
        pp.next = curr
        pp = p
        p = p.next
        if not p:
            return dummy
        curr = p.next
    return dummy


def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next


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
k = 4
print(swap_pairs(a).printList())
# print(reverseKGroup(a, k).printList())


def reverse_between(head, left, right):
    cnt = 1
    curr = head
    prev = ListNode(0)
    prev.next = head
    dummy = prev
    while curr:
        if cnt == left:
            prev = reverse(prev, left, right)
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
        cnt += 1
    print(prev.val)
    return dummy.next


def reverse(prev, left, right):
    last = prev.next
    curr = last.next
    cnt = right - left
    while cnt > 0:
        last.next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = last.next
        cnt -= 1
        # print(last.val)
        # print(prev.val)
        # print()
    return last


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(4)
# g = ListNode(3)
# h = ListNode(2)
# i = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# f.next = g
# g.next = h
# h.next = i
# e.next = None
head = a
left = 1
right = 4
# print(reverse_between(head, left, right).printList())
