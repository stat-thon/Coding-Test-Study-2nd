from collections import Counter
def solution(want, number, discount):
    cnt = 0
    for i in range(len(discount)-9):
        dic = Counter(discount[i:i+10])

        for j in range(len(want)):
            dic[want[j]] -= number[j]

        if all(c == 0 for c in dic.values()):
            cnt += 1
        
    return cnt
