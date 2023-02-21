def solution(number, limit, power):
    store = 0
    for j in range(1, number+1):
        a = yak(j)
        if a <= limit:
            store += a
        else:
            store += power
    return store

def yak(n):
    data = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            data.add(i)
            data.add(n // i)
    return len(data)
