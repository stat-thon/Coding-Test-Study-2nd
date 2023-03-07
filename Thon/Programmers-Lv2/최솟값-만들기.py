def solution(A, B):
    result = 0
    for a, b in zip(sorted(A), sorted(B, reverse = True)):
        result += a * b
    
    return result