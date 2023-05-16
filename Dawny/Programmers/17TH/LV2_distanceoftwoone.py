def solution(r1, r2):
    x = 1
    cnt = 0
    while x <= r2:
        y2 = (r2**2 - x**2) ** 0.5
        y1 = (r1**2 - x**2) ** 0.5 if r1 >= x else 0
        cnt += int(y2) - int(y1) + 1 if y1 == int(y1) else int(y2) - int(y1)
        x += 1
    return cnt*4
