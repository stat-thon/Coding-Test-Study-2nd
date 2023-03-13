def solution(k, tangerine):
    c=0
    box=dict()
    for i in set(tangerine) :
        box[i]=0
    for i in tangerine :
        box[i] +=1
    print(box)
    box=sorted(box.items(), key=lambda x: x[1],reverse=True)
    print(box)
    for i, j in enumerate(box):
        c += j[1]
        if c >= k :
            return i+1
