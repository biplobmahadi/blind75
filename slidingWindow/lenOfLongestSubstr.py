def lenOfLongestSubstr(s):
    longest = 0
    for i in range(len(s)):
        hashMap = {}
        for j in range(i, len(s)):
            if s[j] not in hashMap:
                hashMap[s[j]] = True
            else:
                break
        longest = max(longest, len(hashMap))
    return longest

def lenOfLongestSubstrOptimal(s):
    hashSet, longest, l = set(), 0, 0
    for r in range(len(s)):
        while s[r] in hashSet:
            hashSet.remove(s[l])
            l+=1
        longest = max(longest, r-l+1)
        hashSet.add(s[r])
    return longest

print(lenOfLongestSubstr('abcabcbb'))
print(lenOfLongestSubstrOptimal('abcabcbb'))