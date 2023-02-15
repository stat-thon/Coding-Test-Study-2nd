# input
n, *c = map(int, open(0).read().split())

f = [1] * n
b = [1] * n
for i in range(n):
    for j in range(i):
        if c[i] > c[j]:
            f[i] = max(f[i], f[j]+1)
        if c[n-1-i] > c[n-1-j]:
            b[n-1-i] = max(b[n-1-i], b[n-1-j]+1)

print(max(list(map(lambda x, y: x+y-1, f, b))))
