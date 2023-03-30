def solution(n):
    # 공간
    r = [[0 for _ in range(k)] for k in range(1, n+1)]
    
    # 방향
    dic = {'D':[1, 0], 'R':[0, 1], 'U':[-1, -1]}
    
    # 지점
    place = [-1, 0]
    
    # 넣을 변수
    cnt = 0
    
    # 진행 방향
    sign = 'D'
    
    # 돌림
    for i in range(n, 0, -1):
        for a in range(i, 0, -1):
            cnt += 1
            place[0] += dic[sign][0]
            place[1] += dic[sign][1]
            r[place[0]][place[1]] = cnt
        if sign == "D":
            sign = "R"
        elif sign == "R":
            sign = "U"
        else:
            sign = "D"
        
    return sum(r, [])
