# module
from collections import deque

# input
n = int(input())

time = deque([])
for _ in range(n):
    time.append(list(map(int, input().split())))

time = deque(sorted(time, key=lambda x: (x[1], x[0])))

classopen = [[0, 0]]
while time:
    s, e = time.popleft()
    if classopen[-1][1] <= s:
        classopen.append([s, e])

print(len(classopen)-1)
