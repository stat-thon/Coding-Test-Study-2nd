# input
n = int(input())

# dp
ez = [[0]*10 for s in range(n+1)]
for k in range(1, 10):
    ez[1][k] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            ez[i][j] = ez[i-1][j+1]
        elif j == 9:
            ez[i][j] = ez[i-1][j-1]
        else:
            ez[i][j] = ez[i-1][j+1] + ez[i-1][j-1]

print(sum(ez[n]) % 1000000000)

# dp (0, 9), (1, 8), (2, 7), (3, 6), (4, 5)
case = [0, (1, 2, 2, 2, 2), (2, 3, 4, 4, 4)]
mod = 1000000000

if n <= 2:
    print(sum(case[n]))

else:
    for _ in range(n-2):
        a, b, c, d, e = case[-1]
        case.append((b, (a+c) % mod, (b+d) % mod, (c+e) % mod, (d+e) % mod))
    print(sum(case[n]) % mod)
