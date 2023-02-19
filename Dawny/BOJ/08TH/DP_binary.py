# input
n, k = map(int, input().split())

# dp
space = [[1] + [0 for _ in range(n)] for _ in range(n+1)]


# bottom up
for i in range(1, n+1):
    for j in range(1, n+1):
        space[i][j] = space[i-1][j-1] + space[i-1][j] 

print(space[n][k] % 10007)
