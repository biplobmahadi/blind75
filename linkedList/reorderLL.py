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

def reorderOptimal(head: ListNode):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev
    first = head 
    while second:
        nxtFirst, nxtSecond = first.next, second.next
        first.next = second
        second.next = nxtFirst
        second = nxtSecond
        first = nxtFirst