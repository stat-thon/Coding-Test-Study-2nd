# 깔끔한 정답 풀이 (답 찾아봄)
import sys
from collections import deque

start, end = map(int, input().split())
dist = [0] * 100001

dq = deque()
dq.append(start)
dist[start] = 1 # time 기록 + visit 기능 한번에

while dq:
    qx = dq.popleft()

    if qx == end:
        print(dist[end] - 1)
        break

    for nx in (2 * qx, qx - 1, qx + 1):
        if 0 <= nx < 100001 and dist[nx] == 0:
            if nx == 2 * qx:
                dist[nx] = dist[qx]
                dq.appendleft(nx)
            else:
                dist[nx] = dist[qx] + 1
                dq.append(nx)


###################
# 내 풀이 (시간초과)
# 시간초과 나오는 내 풀이
# 테스트케이스는 다 통과하는데.. 시간초과 해결 못 했음
# 2의 거듭제곱 곱한 값을 전부 큐에 추가해서 효율이 매우 떨어지는 듯
start, end = map(int, input().split())

from collections import deque
import sys

visit = []
dq = deque()
n = 0

while start * 2 ** (n - 1) < end:
    dq.append((start * 2 ** n, 0))
    visit.append(start * 2 ** n)
    if start * 2 ** n == end:
        print(0)
        sys.exit()
    n += 1

dx = [-1, 1]

while dq:
    qx, dist = dq.popleft()
    
    if qx == end:
        break
    
    elif qx > end:
        nx = qx - 1

        if nx == end:
            print(dist + 1)
            sys.exit()

        if nx not in visit:
            dq.append((nx, dist + 1))
            visit.append(nx)

    else:
        for d in range(2):
            nx = qx + dx[d]

            if nx == end:
                print(dist + 1)
                sys.exit()

            if nx > 0:
                n = 0
                while nx * 2 ** (n - 1) < end:

                    if nx * 2 ** n not in visit:
                        if nx * 2 ** n == end:
                            print(dist + 1)
                            sys.exit()
                        dq.append((nx * 2 ** n, dist + 1))
                        visit.append(nx * 2 ** n)
                    n += 1
                    

print(dist)