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
    
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))