def reverseBit(n):
    res = 0
    for i in range(32):
        bit = n & 1
        n = n >> 1
        res = res | (bit << (31-i))
    return res

print(reverseBit(43261596))
