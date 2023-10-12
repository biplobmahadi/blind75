class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder(head: ListNode):
    curr = head
    while curr:
        prev = curr
        tail = curr.next
        while tail and tail.next:
            prev = tail
            tail = tail.next
        prev.next = None
        nxt = curr.next
        curr.next = tail
        curr = nxt
        if tail: tail.next = nxt
