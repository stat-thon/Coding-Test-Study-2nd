# input
item, limit = map(int, input().split())

weight = []
value = []
for i in range(item):
    a, b = map(int, input().split())
    weight.append(a)
    value.append(b)

# back
back = [[0]*(limit + 1) for _ in range(item + 1)]

# original
for j in range(1, item + 1):
    for k in range(1, limit + 1):
        w = weight[j - 1]
        v = value[j - 1]

        if k < w:
            back[j][k] = back[j - 1][k]
        else:
            back[j][k] = max(v + back[j - 1][k - w], back[j - 1][k])

print(back[item][limit])
