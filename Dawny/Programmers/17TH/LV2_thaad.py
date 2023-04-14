def solution(routes):
    car = sorted(routes, key = lambda x: (x[1], x[0]))
    stack = [-0.1]
    for i in car:
        if stack[-1] > i[0]:
            continue
        stack.append(i[1])
    return len(stack) - 1
