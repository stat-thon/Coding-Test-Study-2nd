# input
n = int(input())

# dp
a = 0
b = 1
for _ in range(n):
    a, b = b % 15746, (a+b) % 15746
print(b)
