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
