class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        curr = self
        while curr:
            print(curr.val, end=" ")
            curr = curr.next


def swap_nodes(head, k):
    curr = head
    cnt = 0
    end, start = None, None
    while curr:
        cnt += 1
        if end is not None:
            end = end.next
        if cnt == k - 1:
            start = curr
            end = head
        curr = curr.next
    swap(start, end)
    return head


def swap(x, y):
    temp = x.val
    x.val = y.val
    y.val = temp


a = LinkedListNode(3)
b = LinkedListNode(2)
# c = LinkedListNode(3)
# d = LinkedListNode(4)
# e = LinkedListNode(5)
# f = LinkedListNode(6)

a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

print(swap_nodes(a, 2).printList())
