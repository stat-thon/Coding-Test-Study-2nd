# input
n, *c = map(int, open(0).read().split())

# dp
dp = c[:]
for i in range(n):
    for j in range(i):
        if c[i] > c[j]:
            dp[i] = max(dp[i], dp[j] + c[i])

print(max(dp))
