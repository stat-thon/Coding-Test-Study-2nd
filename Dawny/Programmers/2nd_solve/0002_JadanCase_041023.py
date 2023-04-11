# 1st
solution = lambda s: s[0].upper() + ''.join([t.upper() if c == ' ' and t != ' ' else t.lower() for c, t in zip(s[:-1], s[1:])])

# 2nd
def solution(s):
    n = ' '+s
    string = ""
    for i, j in enumerate(n):
        if i == 0:
            pass
        if j != ' ' and n[i-1] == ' ':
            string += j.upper()
        else:
            string += j.lower()
        
    return string[1:]
# 코드가 더 길어졌다.
# 구조는 동일하다.
