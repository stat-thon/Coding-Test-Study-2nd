# input
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

# greedy
print(sum(list(map(lambda x, y: x*y, a, b))))
