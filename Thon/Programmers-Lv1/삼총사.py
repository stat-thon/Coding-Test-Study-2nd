from itertools import combinations
def solution(number):
    result = 0
    for a, b, c in combinations(number, 3):
        if a + b + c == 0:
            result += 1
    return result