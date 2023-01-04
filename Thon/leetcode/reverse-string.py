# 파이썬 알고리즘 인터뷰 6장 2번 문제
# https://leetcode.com/problems/reverse-string/

class Solution:
    # My solution
    def reverseString(self, s):
        s.reverse()
        print(s)

    # Solution 1. Classical Way using Two Pointers
    def solution1(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left] # -> Swap
            left += 1
            right += 1
    
    # Solution 2. Pythonic Way
    def solution2(self, s):
        s.reverse()
        # You don't nee to print(s), because this problem says "you don't need to return"

    # Tip
    def solution3(self, s):
        # s = s[::-1] # It should be work but it doesn't work in leetcode because they constrain memory with O(1)
        # so you need a  trick
        s[:] = s[::-1] # It works