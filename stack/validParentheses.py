def validParentheses(s):
    map, stack = {'(': ')','{': '}','[': ']'}, []
    for c in s:
        if map.get(c):
            stack.append(map[c])
        else:
            if len(stack) > 0:
                popped = stack.pop()
                if popped != c:
                    return False
            else: return False
    return len(stack) == 0

print(validParentheses(')({})'))