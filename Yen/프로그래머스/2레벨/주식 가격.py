def solution(prices):

    n = len(prices)
    answer = [n - i for i in range(1, n + 1)]
    stack = []

    for i, p in enumerate(prices):

        while stack and prices[stack[-1]] > p:
            last = stack.pop()
            answer[last] = i - last

        stack.append(i)

    return answer
