# 파이썬 알고리즘 인터뷰 6장 1번 문제
# https://leetcode.com/problems/valid-palindrome/

class Solution:

    # My solution
    def isPalindrome(self, s):
        a = [i.lower() for i in s if i.isalnum()]
        return a == a[::-1]
    
    # Solution 1
    def solution1(self, s):
        strs = [i.lower() for i in s if i.isalnum()]
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    # Solution 2
    def solution2(self, s):

        from collections import deque
        strs = deque()
    
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
    
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

    # Solution 3.
    def solution3(self, s):
        import re
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

    # 가장 시간이 짧은 풀이 on leetcode
    def solution4(self, s):
        import string
        s = s.translate(str.maketrans('', '', string.punctuation)) #-> 특수문자만 제거
        s = ''.join(s.split()) #-> split 후 join으로 병합 -> 공백 제거
        s = s.lower() # -> 소문자화

        # translate(): 문자열을 변환해줌
        # str.maketrans('원래문자', '대입문자', '제외할문자) -> 원래 문자에 다른 문자를 대입할 때 사용, 제외할 문자는 제외
        # string.punctuation: 모든 특수문자를 말함
        return s == s[::-1]
