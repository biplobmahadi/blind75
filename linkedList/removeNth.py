def removeNth(head, n):
    length, curr = 0, head
    while curr:
        length+=1
        curr = curr.next
    count, curr = 1, head
    while count < length - n:
        curr = curr.next
        count+=1
    if length == n: head = head.next
    else: curr.next = curr.next.next
    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthOptimal(head, n):
    dummy = ListNode(0, head)
    right = head
    while n>0:
        right = right.next
        n-=1
    left = dummy
    while right:
        right = right.next
        left = left.next
    left.next = left.next.next
    return dummy.next
