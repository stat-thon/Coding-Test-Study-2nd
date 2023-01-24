# moduls
from collections import deque

# input
n, k = map(int, input().split())

# make value
visit = [0] * 100001
q = deque([[n, 0]])
visit[n] = 1

# bfs
while q:
    num, sec = q.popleft()
    if num == k:
        print(sec)
        break

    for i in [2*num, num-1, num+1]:
        if 0 <= i <= 100000:
            if visit[i] == 0:
                if i == 2 * num:
                    visit[i] = 1
                    q.appendleft([i, sec])
                else:
                    visit[i] = 1
                    q.append([i, sec+1])


# 진짜 대단한 사람의 답안
def f(start, end):
    if start >= end:
        return start - end
    elif end == 1:
        return 1
    elif end % 2 == 0:
        return min(end - start, f(start, end // 2))
    else:
        return 1+min(f(start, end + 1), f(start, end - 1))


print(f(n, k))
