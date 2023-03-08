class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at
    # head of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)


def reorder_list(head):
    cnt = 0
    dummy = LinkedListNode(0)
    prev = dummy
    curr = head
    prev.next = head

    while curr:
        cnt += 1
        curr = curr.next

    if cnt == 0 or cnt == 1:
        return head
    curr = head
    last = head
    for i in range(cnt):
        if i > cnt / 2 and curr:
            prev.next = last.next
            last.next = curr.next
            curr.next = last
            curr = last.next
        elif curr and i < cnt:
            prev = prev.next
            last = last.next
            curr = curr.next
    t = dummy.next
    curr = prev.next
    while curr:
        prev.next = curr.next
        curr.next = t.next
        t.next = curr
        curr = prev.next
    return dummy.next
