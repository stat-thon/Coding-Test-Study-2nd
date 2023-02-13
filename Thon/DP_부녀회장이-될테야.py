# 다이나믹 프로그래밍
T = int(input())

# define function
def floor_cnt(k, n):
    floor = [i for i in range(1, n + 1)]

    while k:
        
        temp_copy = floor[:]

        k -= 1
        for i in range(n):
            floor[i] = sum(temp_copy[:i + 1])
        
    return floor[n - 1]

# print result
for _ in range(T):
    k = int(input())
    n = int(input())
    print(floor_cnt(k, n))