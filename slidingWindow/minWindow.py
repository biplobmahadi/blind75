def minWindow(s, t):
    if len(s)< len(t) or t == '':
        return ''
    tmap = {}
    for n in t:
        tmap[n] = 1 + tmap.get(n, 0)

    have, need = 0, len(tmap)
    smap, l, res, resLen = {}, 0, [-1, -1], len(s)
    for r in range(len(s)):
        if s[r] in tmap:
            smap[s[r]] = smap.get(s[r], 0) + 1
            if smap[s[r]] == tmap[s[r]]:
                have+=1
        while have == need:
            if resLen >= r-l+1:
                resLen = r-l+1
                res = [l, r]
            if s[l] in smap:
                smap[s[l]] -=1
                if smap[s[l]] < tmap[s[l]]:
                    have-=1
            l+=1
    return s[res[0]:res[1]+1]


print(minWindow('aa', "aa"))
