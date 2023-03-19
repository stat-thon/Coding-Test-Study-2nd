def solution(numbers):
    answer = 0

    find = []
    find_idx = []
    count = 1
    length = 0
    while count <= len(numbers):
        for i in range(length, len(find)):
            for h in range(len(numbers)):
                if str(h) not in str(find_idx[i]):
                    find.append(find[i] + numbers[h])
                    find_idx.append(str(find_idx[i]) + str(h))
        if len(find) == 0:
            for g in range(len(numbers)):
                find.append(numbers[g])
                find_idx.append(str(g))
        count += 1

    find = list(map(int, find))
    find = set(find)
    find = list(find)
    for j in range(len(find)):
        if find[j] == 0 or find[j] == 1:
            continue
        flag = True
        for k in range(2, find[j]):
            if find[j] % k == 0:
                flag = False
                break
        if flag:
            answer += 1

    return answer
