# module
from collections import deque
import heapq

# input
n = int(input())

time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

# greedy
time.sort()
time = deque(time)
classopen = [0]
while time:
    s, e = time.popleft()
    if s < classopen[0]:
        heapq.heappush(classopen, e)
    else:
        heapq.heappop(classopen)
        heapq.heappush(classopen, e)
print(len(classopen))
