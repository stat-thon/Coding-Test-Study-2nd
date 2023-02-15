# input
n = int(input())

# dp
k = [[1] * 10]
for i in range(n-1):
    k.append([1]+[0]*9)

for x in range(1, n):
    for y in range(1, 10):
        k[x][y] = k[x-1][y] + k[x][y-1]

print(sum(k[-1]) % 10007)
