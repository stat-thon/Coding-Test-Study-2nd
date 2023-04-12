from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list)
    g = defaultdict(int)
    for num, music in enumerate(zip(genres, plays)):
        dic[music[0]].append([num, music[1]])
        dic[music[0]].sort(key = lambda x: (x[1], -x[0]))
        if music[0] in g:
            g[music[0]] += music[1]
        else:
            g[music[0]] = music[1]
    
    l = []
    for genre in list(zip(*sorted(g.items(), key = lambda x: -x[1])))[0]:
        cnt = 0
        while dic[genre] and cnt < 2:
            tmp = dic[genre].pop()
            l.append(tmp[0])
            cnt += 1
    return l
