from itertools import combinations
def solution(orders, course):
    o = list(map(sorted, orders))
    dic = {}
    for i in o:
        for j in course:
            for k in combinations(i, j):
                sk = ''.join(k)
                if sk in dic:
                    dic[sk] += 1
                else:
                    dic[sk] = 1
    
    space = [1] * (course[-1] + 1)
    menu = []
    for x, y in sorted(dic.items(), key = lambda x: (-x[1], x[0])):
        pass
        if y > space[len(x)]:
            space[len(x)] = y
            menu.append(x)
        elif y == space[len(x)] and y != 1:
            menu.append(x)
    
    return sorted(menu, key = lambda x: x[0:])
