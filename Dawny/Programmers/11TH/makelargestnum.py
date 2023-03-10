from collections import deque

def solution(number, k):
    q = deque(number)
    stack = deque(["10"])
    while q and k > 0:
        a = q.popleft()
        while int(a) > int(stack[-1]) and k > 0:
            stack.pop()
            k -= 1
        stack.append(a)
    stack.popleft()
    return ''.join(list(stack + q)[:len(number)-k])
