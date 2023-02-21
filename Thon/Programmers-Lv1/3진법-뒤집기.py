def solution(n):
    num_str = ''
    while n:
        n, l = divmod(n, 3)
        num_str += str(l)
    
    a = 0
    result = 0
    for s in num_str[::-1]:
        result += int(s) * (3 ** a)
        a += 1
    return result