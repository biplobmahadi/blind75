def alien(words):
    adj = {c: set() for w in words for c in w}
    ind = {c: 0 for w in words for c in w}
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        minL = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minL] == w2[:minL]:
            return ''
        for j in range(minL):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                ind[w2[j]] += 1
                break
    
    stack, res = [], ''
    for n in ind:
        if ind[n] == 0:
            stack.append(n)
    while stack:
        p = stack.pop()
        res += p
        for nei in adj[p]:
            ind[nei] -= 1
            if ind[nei] == 0: stack.append(nei)
    return res

print(alien(["wrt","wrf","er","ett","rftt"]))