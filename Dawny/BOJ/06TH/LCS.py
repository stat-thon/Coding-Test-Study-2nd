# input
f = input()
s = input()

lcs = [[0 for _ in range(len(s) + 1)] for _ in range(len(f) + 1)]

for i in range(1, len(f)+1):
    for j in range(1, len(s)+1):
        if f[i - 1] == s[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[-1][-1])
