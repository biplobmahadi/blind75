s = 'A man, a plan, a canal: Panama'

def isValid(s: str):
    l, r = 0, len(s) - 1
    while r>l:
        if s[r].isalnum() and s[l].isalnum():
            if s[r].upper() != s[l].upper():
                return False
            l+=1
            r-=1
        else:
            if not s[r].isalnum():
                r-=1
            if not s[l].isalnum():
                l+=1
    return True

print(isValid('   '))