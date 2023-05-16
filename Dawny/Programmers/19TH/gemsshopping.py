from collections import defaultdict
def solution(gems):
    cnt = defaultdict(lambda : 0)
    gemtype = len(set(gems))
    g = len(gems)
    l = 0
    r = 0
    rangenum = []
    while True:
        if l > r:
            break
        elif len(cnt) == gemtype:
            rangenum.append([l + 1, r])
            cnt[gems[l]] -= 1
            if cnt[gems[l]] == 0:
                del cnt[gems[l]]
            l += 1
        elif r == g:
            break
        else:
            cnt[gems[r]] += 1
            r += 1
    
    dab = [1, g]
    for i in rangenum:
        if (i[1] - i[0]) < (dab[1] - dab[0]):
            dab = i
        
    return dab
