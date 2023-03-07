def solution(s):
    dic = {}
    for i in s.replace("{",",").replace("}",",").split(","):
        if i != "":
            k = int(i)
            if k in dic:
                dic[k] += 1
            else:
                dic[k] = 1
    
    return list(list(zip(*sorted(dic.items(), key = lambda x: -x[1])))[0])
