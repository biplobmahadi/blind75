def isAnagram(s: str, t: str):
    if len(s) == len(t):
        li = list(s)
        for n in t:
            findIndex = None
            for i in range(len(li)):
                if li[i] == n:
                    findIndex = i
            if findIndex is not None:
                li[findIndex] = None
            else:
                return False
        return True
    else:
        return False
    
s = "rat"
t = "car"
print(isAnagram(s, t))

def isAnagramOptimal(s: str, t: str):
    if len(s) != len(t): return False
    mapS, mapT = {}, {}
    for i in range(len(s)):
        mapS[s[i]] = mapS.get(s[i], 0) + 1
        mapT[t[i]] = mapT.get(t[i], 0) + 1
    print(mapS, mapT)
    for n in mapS:
        if mapS[n] != mapT.get(n, 0): return False
    return True

print(isAnagramOptimal(s, t))
