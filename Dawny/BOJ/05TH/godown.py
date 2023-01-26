# input
n = int(input())

max_pan = [0, 0, 0]
min_pan = [0, 0, 0]

max_p = [0, 0, 0]
min_p = [0, 0, 0]

# dp
for i in range(n):
    max_p = max_pan.copy()
    min_p = min_pan.copy()
    a, b, c = list(map(int, input().split()))
    max_pan[0] = a + max(max_p[0], max_p[1])
    min_pan[0] = a + min(min_p[0], min_p[1])
    max_pan[1] = b + max(max_p[0], max_p[1], max_p[2])
    min_pan[1] = b + min(min_p[0], min_p[1], min_p[2])
    max_pan[2] = c + max(max_p[1], max_p[2])
    min_pan[2] = c + min(min_p[1], min_p[2])

print(max(max_pan), min(min_pan))
