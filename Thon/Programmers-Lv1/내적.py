def solution(a, b):
    result = 0
    for i, j in zip(a, b):
        result += i * j
    return result