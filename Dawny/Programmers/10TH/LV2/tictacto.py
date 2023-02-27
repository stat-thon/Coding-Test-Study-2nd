def solution(board):
    count_O = 0
    count_X = 0
    maps_O = [[0] * 3 for _ in range(3)]
    maps_X = [[0] * 3 for _ in range(3)]
    for r, i in enumerate(board):
        for c, j in enumerate(i):
            if j == "O":
                count_O += 1
                maps_O[r][c] = 1
            elif j == "X":
                count_X += 1
                maps_X[r][c] = 1
    
    maps_O_reverse = [list(x) for x in zip(*maps_O)]
    maps_X_reverse = [list(x) for x in zip(*maps_X)]
    cnt = count_O - count_X
    
    # nogada
    O = []
    X = []
    for k in range(3):
        O.append(sum(maps_O[k]))
        O.append(sum(maps_O_reverse[k]))
        X.append(sum(maps_X[k]))
        X.append(sum(maps_X_reverse[k]))
    O.append(maps_O[0][0] + maps_O[1][1] + maps_O[2][2])
    X.append(maps_X[0][0] + maps_X[1][1] + maps_X[2][2])
    O.append(maps_O[2][0] + maps_O[1][1] + maps_O[0][2])
    X.append(maps_X[2][0] + maps_X[1][1] + maps_X[0][2])

    if cnt == 1 and X.count(3) == 0:
        return 1
    elif cnt == 0 and O.count(3) == 0:
        return 1
    else:
        return 0
