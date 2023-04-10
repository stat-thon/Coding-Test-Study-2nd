# 1st
def solution(s):
    
    def convert(s, z, r):
        
        # 0제거 후 길이
        ch = bin(s.count("1"))[2:]
        
        # z: 회전 수, r: 0 제거 개수 
        return [z,r+s.count("0")] if ch == s else convert(ch, z+1, r+s.count("0"))
    
    return convert(s, 0, 0)
  
# 2nd
def solution(s):
    a = [0, 0]
    while int(s) > 1:
        a[0] += 1
        l = len(s)
        s = "1"*s.count("1")
        a[1] += l - len(s)
        s = bin(len(s))[2:]
    return a
  
# 1st는 재귀 2nd는 반복법을 활용해 풀었는데 이 문제에서는 재귀가 속도가 훨씬 빠르다.
# 재귀함수에 대해서 다시한번 복습해 볼 수 있는 코드였다.
