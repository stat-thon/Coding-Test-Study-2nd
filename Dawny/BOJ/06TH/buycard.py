# input
n = int(input())
p = [0] + list(map(int, input().split()))

price = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        price[i] = max(price[i], price[i-j] + p[j])
print(price)
