def solution(keymap, targets):
    result = []
    dic = {}
    for i in keymap:
        for j, k in enumerate(i):
            if k in dic and dic[k] > j+1:
                dic[k] = j+1
            else:
                dic.setdefault(k, j+1)
                
    for x in targets:
        a = 0
        for y in x:
            if y in dic:
                a += dic[y]
            else:
                a = -1
                break
        result.append(a)
    return result
