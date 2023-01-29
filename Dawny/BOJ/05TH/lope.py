# input
n = int(input())

lope = []
for _ in range(n):
    lope.append(int(input()))

# sort
lope.sort()

# find weight
print(max(list(map(lambda x, s: x*(n-s), lope, range(n)))))
