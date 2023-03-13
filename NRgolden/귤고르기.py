def solution(k, tangerine):
    tangerine_cnt = []
    tmp=''
    answer=0
    index =0
    for i,t in enumerate(sorted(tangerine)):
        if tmp=='':
            tmp = t
            continue
        if tmp!=t:
            tangerine_cnt.append(i - index)
            tmp = t
            index = i
    tangerine_cnt.append(i- index +1)
    cnt_lst = sorted(tangerine_cnt,reverse=True)
    cnt =0
    for i in cnt_lst:
        if cnt<k:
            cnt+=i
            answer+=1
        else:
            break
    return answer
