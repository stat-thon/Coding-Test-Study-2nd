from collections import deque
def solution(order):
    cnt = 0
    q = deque(list(range(1, len(order) + 1)))
    truck = deque(order)
    stack = [0]
    while truck:
        if stack[-1] == truck[0]:
            stack.pop()
            truck.popleft()
            cnt += 1
        elif q and q[0] == truck[0]:
            q.popleft()
            truck.popleft()
            cnt += 1
        elif q:
            stack.append(q.popleft())
        else:
            break
                
    return cnt
