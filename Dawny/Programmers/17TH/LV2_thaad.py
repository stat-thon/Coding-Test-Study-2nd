def solution(targets):
    t = sorted(targets, key = lambda x: (x[1], x[0]))
    stack = [0]
    for i in t:
        if stack[-1] > i[0]:
            continue
        stack.append(i[1])
    return len(stack) - 1
