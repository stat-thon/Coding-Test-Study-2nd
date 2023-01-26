# input
t = int(input())

# dp
a = [1, 1]
for i in range(2, 30):
    a.append(i*a[-1])

# output
for _ in range(t):
    n, m = map(int, input().split())
    print(a[m] // (a[n] * a[m-n]))
