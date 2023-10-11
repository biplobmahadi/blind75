def reverseLL(head):
    current, hold = head, None
    while current:
        nextNode = current.next
        current.next = hold
        hold = current
        current = nextNode
    return hold
