# input
n = int(input())
time = []
value = []
for _ in range(n):
    t, v = list(map(int, input().split()))
    time.append(t)
    value.append(v)

# value
money = [0] * (n+1)

# dp
for i in range(n-1, -1, -1):
    if time[i]+i <= n:
        money[i] = max(value[i] + money[i+time[i]], money[i+1])
    else:
        money[i] = money[i+1]

print(money[0])
