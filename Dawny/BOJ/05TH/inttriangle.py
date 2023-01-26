# input
n = int(input())

triangle = [[0, 0]]
for _ in range(n):
    triangle.append([0]+list(map(int, input().split()))+[0])

# dp
for i in range(1, n+1):
    for j in range(1, i+1):
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[-1]))
