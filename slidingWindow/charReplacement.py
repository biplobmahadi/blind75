def charReplacement(s, k):
    hashMap, res, l = {}, 0, 0
    for r in range(len(s)):
        hashMap[s[r]] = hashMap.get(s[r], 0) + 1
        maxF = max(hashMap.values())
        window = r-l+1
        diff = window - maxF
        if diff > k:
            hashMap[s[l]] -= 1
            l+=1
        else:
            res = max(res, window)
    return res

print(charReplacement('ABCDE', 2)) 