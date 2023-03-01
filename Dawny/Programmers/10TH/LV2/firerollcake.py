def solution(topping):
    if len(set(topping)) == 1:
        return len(set(topping)) - 1
    s = {}
    f = set()
    cnt = 0
    
    for i in topping:
        s[str(i)] = s.get(str(i), 0)
        s[str(i)] += 1
        
    for i in topping:
        f.add(i)
        s[str(i)] -= 1
        if s[str(i)] == 0:
            del s[str(i)]
        if len(f) == len(s.keys()):
            cnt += 1
        elif len(f) > len(s):
            break
            
    return cnt
