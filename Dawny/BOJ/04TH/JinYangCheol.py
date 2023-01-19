# moduls
import sys
from collections import deque

# input
n = int(input())

# friends line
friend = [[] for _ in range(n)]
while True:
    x, y = map(int, sys.stdin.readline().split())
    if x == -1:
        break
    friend[x-1].append(y-1)
    friend[y-1].append(x-1)


# bfs
def bfs(num):
    q = deque([[num, 0]])
    visit = [0 for _ in range(n)]
    visit[num] = 1
    max_cnt = 0
    while q:
        node, cnt = q.popleft()
        if cnt > max_cnt:
            max_cnt = cnt

        for i in friend[node]:
            if visit[i] == 0:
                visit[i] = 1
                q.append([i, cnt+1])

    return max_cnt


score = []
min_score = 51
for j in range(n):
    result = bfs(j)
    if min_score == result:
        score.append(j+1)
    elif min_score > result:
        min_score = result
        score = [j+1]

print(min_score, len(score))
print(*score)
