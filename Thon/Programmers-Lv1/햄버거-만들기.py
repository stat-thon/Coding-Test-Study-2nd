def solution(ingredient):
    stack = []
    result = 0
    for i in ingredient:
        stack.append(i)
        
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            result += 1
    return result