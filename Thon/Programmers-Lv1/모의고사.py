def solution(answers):
    
    rule = [[1, 2, 3, 4, 5], 
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    cnts = [0] * 3
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == rule[j][i % len(rule[j])]:
                cnts[j] += 1

    return [i + 1 for i in range(3) if cnts[i] == max(cnts)]