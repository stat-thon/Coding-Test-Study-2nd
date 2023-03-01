from functools import *
def solution(data, col, row_begin, row_end):
    h = []
    for i, j in enumerate(sorted(data, key = lambda x: (x[col-1], -x[0]))[row_begin-1:row_end]):
        h.append(sum(list(map(lambda x: x % (i+row_begin), j))))
    
    return reduce(lambda x, y: x^y, h)
