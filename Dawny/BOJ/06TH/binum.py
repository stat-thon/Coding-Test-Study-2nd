target = int(input())

# 걍 피보나치다
a = 1
b = 1
for i in range(target-1):
    a, b = b, a+b

print(a)
