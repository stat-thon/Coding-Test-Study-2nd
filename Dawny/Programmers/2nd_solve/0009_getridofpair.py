# 1st
from collections import deque

def solution(s):
    
    # s 없으면 1
    if not s:
        return 1
    
    # 길이가 홀수면 0 : 아무리 짝지어도 홀수개면 없어질 수 없음
    elif len(s) % 2 == 1:
        return 0
    
    # 스택 알고리즘으로 해결
    stack = deque()
    s = deque(s)
    
    # 모든 글자가 뽑힐 때 까지 반복
    while s:
        tmp = s.popleft()
        # 빈공간에 아예 없거나 새로뽑은 글자가 기존 담긴 글자의 마지막과 다르면 스택
        if not stack or stack[-1] != tmp:
            stack.append(tmp)
            
        # 새로뽑은 글자가 기존 담긴 글자의 마지막과 같으면 팝
        else:
            stack.pop()
    
    # 글자가 남아있으면 제거하지 못함
    if stack:
        return 0
    
    # 아니라면 제거 완료
    return 1
    
# 2nd
from collections import deque

def solution(s):
    stack = []
    q = deque(s)
    while q:
        a = q.popleft()
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)

    return 0 if stack else 1
  
# 스택 방법도 어느정도 익숙해진듯 하다. 문제 자체가 스택이라는 것을 한눈에 볼 수 있었다.
