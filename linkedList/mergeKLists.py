from collections import defaultdict

def mergeKLists(lists):
    hashMap = defaultdict(list)
    for n in lists:
        while n:
            nxt = n.next
            n.next = None
            hashMap[n.val].append(n)
            n = nxt
    print(hashMap)
    head = tail = ListNode()
    for _ in range(len(hashMap)):
        minVal = min(hashMap.keys())
        for n in hashMap[minVal]:
            tail.next = n
            tail = n
        del hashMap[minVal]
    return head.next

# O(nlogk) and O(k)
def mergeKLists2(lists):
    if not lists or len(lists) == 0:
        return None
    while len(lists)>1:
        mergedList = []
        for i in range(len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1<len(lists) else None
            mergedList.append(merge2(l1, l2))
        lists = mergedList
    return lists[0]

def merge2(l1, l2):
    head = tail = ListNode()
    while l1 and l2:
        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return head.next
