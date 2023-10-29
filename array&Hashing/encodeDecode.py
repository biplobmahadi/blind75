class Solution:
    def encode(self, strs):
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != '#': j+=1
            n = int(str[i: j])
            res.append(str[j+1: j+1+n])
            i = j+1+n
        return res

s = Solution()
print(s.encode(['8iplo###', '###5423', '342#23']))
print(s.decode('8#8iplo###7####54236#342#23'))
