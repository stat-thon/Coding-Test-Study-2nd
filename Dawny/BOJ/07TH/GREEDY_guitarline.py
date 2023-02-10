# input
n, m = map(int, input().split())
sixset = []
one = []
for _ in range(m):
    a, b = map(int, input().split())
    sixset.append(a)
    one.append(b)

s = min(sixset)
o = min(one)
if s >= o*6:
    print(o*n)
elif n % 6 == 0:
    print(s*(n // 6))
else:
    print(s*(n // 6) + s if s <= o*(n % 6) else s*(n // 6) + o*(n % 6))
