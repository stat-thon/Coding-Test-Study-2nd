def solution(t, p):
    
    return len([t[c:c+len(p)] for c in range(len(t)-len(p)+1) if int(t[c:c+len(p)]) <= int(p)])
