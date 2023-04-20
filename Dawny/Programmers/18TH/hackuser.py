import re
from itertools import permutations
def solution(user_id, banned_id):
    n = len(banned_id)
    b = list(map(lambda x: x.replace("*", "."), banned_id))
    cnt = 0
    visit = []
    for i in permutations(user_id, n):
        for a in range(n):
            if not re.fullmatch(b[a], i[a]):
                break
        else:
            if sorted(i) not in visit:
                visit.append(sorted(i))
                cnt += 1
    
    return cnt
