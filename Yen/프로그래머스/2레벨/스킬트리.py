from collections import deque
def solution(skill, skill_trees):
    q_tree=deque(skill_trees)
    c=0
    while q_tree :
        q=deque(skill)
        a=deque()
        i=q_tree.popleft()
        for j in i :
            if j in skill :
                a.append(j)
                
        while a:
            if q.popleft() != a.popleft():
                if a==deque():
                    c -=1
                break
        if a==deque():
            c +=1
            
    return c
