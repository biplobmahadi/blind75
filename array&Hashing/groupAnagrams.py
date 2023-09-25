from collections import defaultdict
def isAnagramOptimal(s: str, t: str):
    if len(s) != len(t): return False
    mapS, mapT = {}, {}
    for i in range(len(s)):
        mapS[s[i]] = mapS.get(s[i], 0) + 1
        mapT[t[i]] = mapT.get(t[i], 0) + 1
    for n in mapS:
        if mapS[n] != mapT.get(n, 0): return False
    return True

def groupAnagrams(strs: list):
    map, li = {}, []
    for i in range(len(strs)):
        isAna = False
        for j in range(i):
            if isAnagramOptimal(strs[i], strs[j]):
                isAna = True
                li[map[strs[j]]].append(strs[i])
                break
        if not isAna:
            map[strs[i]] = len(li)
            li.append([strs[i]])
    return li
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

def groupAnagramsOptimal(strs: list):
    res = defaultdict(list)
    for n in strs:
        count = [0] * 26
        for c in n:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(n)
    return res.values()

print(groupAnagramsOptimal(strs))