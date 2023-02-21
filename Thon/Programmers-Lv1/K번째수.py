def solution(array, commands):
    answer = []
    
    for a, b, c in commands:
        answer.append(sorted(array[a - 1: b])[c - 1])
    return answer