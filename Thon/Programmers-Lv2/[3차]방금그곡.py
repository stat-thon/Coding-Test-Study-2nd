def solution(m, musicinfos):
    
    shap_dict = {'C': 'H', 'D': 'I', 'F': 'J', 'G': 'K', 'A': 'L', 'E': 'M'}
    # m 처리
    mq = list(m)
    new_m = ''
    while mq:
        am = mq.pop()
        if am != '#':
            new_m = am + new_m
        else:
            new_m = shap_dict[mq.pop()] + new_m
    
    MAX = 0
    song = '(None)'
    for info in musicinfos:
        s, e, title, melody = info.split(',')
        sh, sm, eh, em = int(s[0:2]), int(s[3:]), int(e[0:2]), int(e[3:])
        time = (eh - sh) * 60 + em - sm
        
        q = list(melody)
        new_melody = ''
        while q:
            a = q.pop()
            if a != "#":
                new_melody = a + new_melody
            else:
                new_melody = shap_dict[q.pop()] + new_melody
        if time != 0:
            div, mod = divmod(time, len(new_melody))

            if new_m in new_melody * div + new_melody[:mod]:
                if MAX < time:
                    MAX = time
                    song = title
                
    return song

# 오랜만에 풀어봄
# E# 조건 없었는데 왜 있음?