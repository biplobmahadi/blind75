def validParentheses(s):
    map, stack = {'(': ')','{': '}','[': ']'}, []
    for c in s:
        if map.get(c):
            stack.append(map[c])
        elif not stack or stack.pop() != c:
            return False
    return len(stack) == 0

print(validParentheses('({})('))