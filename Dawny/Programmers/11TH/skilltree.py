from collections import deque

def solution(skill, skill_trees):
    cnt = 0
    for i in skill_trees:
        q = deque(i)
        s = deque(skill)
        while q:
            a = q.popleft()
            if s:
                t = s.popleft()
                if a in s:
                    q.append(a)
                    break
                elif a != t:
                     s.appendleft(t)

        if not q:
            cnt += 1
    
    return cnt
