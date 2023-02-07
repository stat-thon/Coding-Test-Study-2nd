# module
import sys
from collections import deque
input2 = sys.stdin.readline


# bfs
def bfs():
    q = deque([0])
    while q:
        a = q.popleft()
        if a == n+1:
            return True
        for k in range(n+2):
            if possible[a][k] == 1:
                q.append(k)
                possible[a][k] = possible[k][a] = 0
    return False


# input
t = int(input2())
for _ in range(t):
    n = int(input2())
    possible = [[0 for _ in range(n+2)] for _ in range(n+2)]

    # input locate
    locate = []
    for i in range(n+2):
        loc = list(map(int, input2().split()))

        if bool(i):
            for j in range(len(locate)):
                hap = abs(loc[0] - locate[j][0]) + abs(loc[1] - locate[j][1])
                if hap <= 1000:
                    possible[j][i] = possible[i][j] = 1

        locate.append(loc)
    if bfs():
        print("happy")
    else:
        print("sad")
