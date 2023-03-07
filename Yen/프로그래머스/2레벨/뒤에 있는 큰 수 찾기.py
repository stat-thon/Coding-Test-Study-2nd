def solution(numbers):
    answer = [-1] * len(numbers)
    a = []
    for i in range(len(numbers)):
        while a and numbers[a[-1]] < numbers[i]:
            j = a.pop()
            answer[j] = numbers[i]
        a.append(i)

    return answer
