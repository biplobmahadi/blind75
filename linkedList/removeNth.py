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