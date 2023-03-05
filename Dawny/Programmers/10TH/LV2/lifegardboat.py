from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort()
    q = deque(people)
    while q:
        cnt +=1
        a = q.pop()
        if q and q[0] + a <= limit:
            q.popleft()

    return cnt
