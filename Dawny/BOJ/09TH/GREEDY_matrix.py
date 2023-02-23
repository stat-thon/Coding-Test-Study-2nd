# module
import sys
input2 = sys.stdin.readline

# input
n, m = map(int, input2().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input2().rstrip("\n"))))

for _ in range(n):
    b.append(list(map(int, input2().rstrip("\n"))))


# greedy
def change(matrix, i, j):
    for k in range(i, i+3):
        for l in range(j, j+3):
            matrix[k][l] = 1 - matrix[k][l]
    return matrix


if n < 3 or m < 3:
    if a == b:
        print(0)
    else:
        print(-1)
else:
    cnt = 0
    for x in range(n-2):
        for y in range(m-2):
            if a[x][y] != b[x][y]:
                a = change(a, x, y)
                cnt += 1

    if a == b:
        print(cnt)
    else:
        print(-1)
