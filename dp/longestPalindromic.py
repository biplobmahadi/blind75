def longestPalindrome(self, s: str) -> str:
    lenght = 0
    res = [0, 0]
    for i in range(len(s)):
        l, r = i, i
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r-l+1 > lenght:
                lenght = r-l+1
                res = [l, r]
            l-=1
            r+=1
        l, r = i, i+1
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r-l+1 > lenght:
                lenght = r-l+1
                res = [l, r]
            l-=1
            r+=1
    return s[res[0]:res[1]+1]