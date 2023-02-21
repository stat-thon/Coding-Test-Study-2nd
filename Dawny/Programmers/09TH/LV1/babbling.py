def solution(babbling):
    cnt = 0
    sound = ['aya', 'ye', 'woo', 'ma']
    doublesound = ['ayaaya', 'yeye', 'woowoo', 'mama']
    for i in babbling:
        for j in doublesound:
            i = i.replace(j, 'n')
        for k in sound:
            i = i.replace(k, '0')
        if all(c == '0' for c in i):
            cnt += 1
    return cnt
