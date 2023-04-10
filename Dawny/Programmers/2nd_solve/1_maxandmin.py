# ================ 1st answer ===================
def solution(s):
    b = list(map(int,s.split(' ')))
    return str(min(b))+' '+str(max(b))
  
# ================ 2nd answer ===================
def solution(s):
    
    return str(min(list(map(int, s.split(' '))))) + ' ' + str(max(list(map(int, s.split(' ')))))
# ===============================================
## 차이 없음
