N = int(input())

result = 0
if N in [4, 7]:
    result = -1

else:
    if N % 5 == 0:
        result = N // 5
    elif N % 5 in [1, 3]:
        result = (N // 5) + 1
    else:
        result = (N // 5) + 2

print(result)
