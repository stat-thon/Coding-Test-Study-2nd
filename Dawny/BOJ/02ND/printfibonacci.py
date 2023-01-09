# packages
import sys

# input
cnt = int(input())

target = []
for _ in range(cnt):
    target.append(int(sys.stdin.readline()))

# DP
fibo0 = [1, 0]
fibo1 = [0, 1]
for k in range(2, 41):
    fibo0.append(fibo0[k - 1] + fibo0[k - 2])
    fibo1.append(fibo1[k - 1] + fibo1[k - 2])

for i in target:
    print(fibo0[i], fibo1[i])
