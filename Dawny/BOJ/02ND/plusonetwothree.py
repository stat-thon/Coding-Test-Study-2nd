# packages
import sys

# input
cnt = int(input())

target = []
for _ in range(cnt):
    target.append(int(sys.stdin.readline()))

# DP
a = [0, 1, 2, 4]
for i in range(4, 11):
    a.append(a[i-1]+a[i-2]+a[i-3])

for k in target:
    print(a[k])
