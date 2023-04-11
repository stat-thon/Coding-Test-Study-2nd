# 1st
def solution(A,B):

    return sum([x*y for x, y in zip(sorted(A), sorted(B,reverse = True))])
  
# 2nd
def solution(A,B):
    
    return sum([a*b for a, b in zip(sorted(A), sorted(B, reverse = True))])
  
# ? 
