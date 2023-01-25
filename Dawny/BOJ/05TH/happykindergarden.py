# input
n, k = map(int, input().split())
tall = list(map(int, input().split()))

# money
c = []
for i in range(1, n):
    c.append(tall[i] - tall[i-1])

c.sort()
print(sum(c[:n-k]))
