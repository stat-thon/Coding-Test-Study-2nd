def solution(numbers):
    score = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            score[stack.pop()] = numbers[i]
        stack.append(i)
    return score
