from collections import deque
def solution(sequence, k):
    dab = [0] * (len(sequence)+1)
    sub = deque([])
    hap = 0
    q = deque(list(enumerate(sequence)))
    while q:
        if hap < k:
            rank, num = q.popleft()
            hap += num
            sub.append(rank)
        elif hap == k:
            if len(dab) > len(sub):
                dab = list(sub)
            hap -= sequence[sub.popleft()]
        else:
            hap -= sequence[sub.popleft()]
            
    while sub:
        if hap == k and len(dab) > len(sub):
            dab = list(sub)
        hap -= sequence[sub.popleft()]
        
    return [min(dab), max(dab)]
