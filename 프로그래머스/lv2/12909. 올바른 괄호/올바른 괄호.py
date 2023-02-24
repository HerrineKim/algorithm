def solution(s):
    answer = True
    braces = s
    stack = []
    for brace in braces:
        if len(stack) == 0:
            stack.append(brace)
        elif stack[-1] == '(' and brace == ')':
            stack.pop()
        else:
            stack.append(brace)
    if len(stack) == 0:
        return True
    else:
        return False