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