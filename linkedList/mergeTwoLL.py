def mergeTwoLL(list1, list2):
    head, tail = None, None
    while list1 or list2:
        if list1 and list2:
            if list1.val <= list2.val:
                if tail: 
                    tail.next = list1
                    tail = tail.next
                else: 
                    head = list1
                    tail = head
                list1 = list1.next
            else:
                if tail: 
                    tail.next = list2
                    tail = tail.next
                else: 
                    head = list2
                    tail = head
                list2 = list2.next
        elif list1:
            if tail: 
                tail.next = list1
                tail = tail.next
            else: 
                head = list1
                tail = head
            list1 = list1.next
        else:
            if tail: 
                tail.next = list2
                tail = tail.next
            else: 
                head = list2
                tail = head
            list2 = list2.next
    return head


def mergeTwo(list1, list2):
    head = tail = ListNode() # suppose I have given this
    while list1 and list2:
        if list2.val >= list1.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    return head.next