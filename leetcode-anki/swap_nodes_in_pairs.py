class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(self, head):

    if not head or not head.next:
        return head
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    last = head
    curr = last.next

    while curr and last:
        last.next = curr.next
        curr.next = prev.next
        prev.next = curr
        prev = last
        last = last.next
        if not last:
            return dummy.next
        curr = last.next
    return dummy.next
