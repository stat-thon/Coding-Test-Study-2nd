# 1st
def solution(n):
    
    two = "0" + bin(n)[2:]
    two2 = two[::-1]
    wher = two2.find("10")
    lst = list(two2)
    print(two2,lst)
    lst[wher] = "0"
    lst[wher+1] = "1"
    k = sorted(lst[0:wher],reverse = True)
    lst[0:wher] = k
    two3 = ''.join(lst)[::-1]
    print(two3)
    return int(two3,2)
  
# 2nd
def solution(n):
    l = bin(n)[2:].count("1")
    while True:
        n += 1
        l2 = bin(n)[2:].count("1")
        if l == l2:
            return n
# 코드 길이와 방법부터 차이가 드러나는 것을 확인할 수 있었다.
# 예전에 어떻게 짰던건지 너무 신기하다.
