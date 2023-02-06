# input
n, k, *coin = map(int, open(0).read().split())

method = [1 if i % coin[0] == 0 else 0 for i in range(k+1)]

for j in coin[1:]:
    for k in range(j, k+1):
        method[k] += method[k-j]
print(method[-1])
