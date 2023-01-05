# input
x = int(input())

# value
d = [0] * (x+1)

# DP
for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
print(d[x])
