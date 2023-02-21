def solution(ingredient):
    stack = []
    cnt = 0
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            cnt += 1
    return cnt
