# input
n, k = map(int, input().split())
coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

# greedy
count = 0
while coin_types:
    coin = coin_types.pop()
    count += k // coin
    k %= coin

print(count)
