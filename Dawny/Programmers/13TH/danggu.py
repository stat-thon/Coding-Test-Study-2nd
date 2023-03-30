def solution(m, n, startX, startY, balls):
    answer = []
    for a, b in balls:
        case = []
        
        # 1
        v = (startX + a) ** 2
        h = abs(startY - b) ** 2
        if h != 0 or startX - a < 0:
            print(1)
            case.append(v + h)
            
        # 2
        v = abs(startX - a) ** 2
        h = (startY + b) ** 2
        if v != 0 or startY - b < 0:
            print(2)
            case.append(v + h)
        
        # 3
        v = (2*m - a - startX) ** 2
        h = abs(startY - b) ** 2
        if h != 0 or startX - a > 0:
            print(3)
            case.append(v + h)
            
        # 4
        v = abs(startX - a) ** 2
        h = (2*n - b - startY) ** 2
        if v != 0 or startY - b > 0:
            print(4)
            case.append(v + h)
        
        print(case)
        answer.append(min(case))
    return answer
