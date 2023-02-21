def solution(s):
    location = {}
    f = []
    for i, c in enumerate(s):
        if c in location:
            f.append(i - location[c])
            location.update({c:i})
        else:
            location.setdefault(c, i)
            f.append(-1)
    return f
