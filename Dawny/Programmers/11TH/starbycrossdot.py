def solution(line):
    point = []
    row = []
    col = []
    for i, c in enumerate(line):
        for j in line[i+1:]:
            if c[0]*j[1] - c[1]*j[0] != 0:
                x = (c[1]*j[2] - c[2]*j[1]) / (c[0]*j[1] - c[1]*j[0])
                y = (c[2]*j[0] - c[0]*j[2]) / (c[0]*j[1] - c[1]*j[0])
                if x % 1 == 0 and y % 1 == 0:
                    row.append(int(y))
                    col.append(int(x))
                    point.append([int(y), int(x)])
    
    cri = list(map(lambda x: [max(row)-x[0], x[1]-min(col)], point))
    answer=[]
    for a in range(max(row)-min(row)+1):
        klist=""
        for b in range(max(col)-min(col)+1):
            if [a, b] in cri:
                klist += '*'
            else:
                klist += '.'
        answer.append(klist)
        
    return answer
