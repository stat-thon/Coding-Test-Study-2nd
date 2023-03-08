from collections import deque

def solution(p):
    # 1
    if p == '':
        return p
    # 2
    u, v = divide(p)
    # 3
    if check(u):
        return u + solution(v)
    # 4
    else:
        temp = '('+solution(v)+')'
        for x in u[1:-1]:
            if x == '(':
                temp += ')'
            else:
                temp += '('
        return temp


def divide(p):
    cnt = 0
    q = deque(p)
    u = ''
    while q:
        a = q.popleft()
        cnt += 1 if a == '(' else -1
        u += a
        if not cnt:
            return u, ''.join(q)


def check(u):
    q = []
    for x in u:
        if not q:
            q.append(x)
        else:
            if x == ')' and q[-1] == '(':
                q.pop()
            else:
                q.append(x)
    if q:
        return False
    return True
