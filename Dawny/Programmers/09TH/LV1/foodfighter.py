def solution(food):
    s = ''
    for i, j in enumerate(food[1:]):
        s += str(i+1)*(j//2)
    
    return s + '0' + s[::-1]
