from collections import deque

def solution(A, B):
    A.sort()
    B.sort()
    q = deque(A)
    cnt = 0
    num = deque(B)
    while num:
        b = num.popleft()
        if b > q[0]:
            q.popleft()
            cnt += 1
    return cnt
