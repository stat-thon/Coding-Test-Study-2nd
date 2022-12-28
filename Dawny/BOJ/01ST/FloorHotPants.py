# input
v, h = map(int, input().split())

# tile
tile = []
for _ in range(v):
    tile.append(list(input()))

# answer
k = 0

# DFS1 by '-'
def dfs1(a, b):
    global k
    if 0 <= b < h:
        if tile[a][b] != '-':
            k += 1
            return

        tile[a][b] = '0'
        dfs1(a, b+1)

    else:
        k += 1
        return

# DFS2 by '|'
def dfs2(a, b):
    global k
    if 0 <= a < v:
        if tile[a][b] != '|':
            k += 1
            return

        tile[a][b] = '0'
        dfs2(a + 1, b)

    else:
        k += 1
        return

# play this function
for i in range(v):
    for j in range(h):
        if tile[i][j] == '-':
            dfs1(i, j)

        elif tile[i][j] == '|':
            dfs2(i, j)

print(k)
