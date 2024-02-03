def hammingWeight(n):
    count = 0
    while n:
        n &= (n-1)
        count+=1
    return count

def countBits(n):
    res = []
    for i in range(n+1):
        res.append(hammingWeight(i))
    return res

print(countBits(5))
