# 파이썬 알고리즘 인터뷰 6장 6번 문제
# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    # Solution
    def longestPalindrome(self, s: str) -> str:
        # determine palindrome and expanding two pointer (left, right)
        def expand(left, right): # two pointer
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right] # return the actual palindrome
        
        # Exception: length 1 word or the word is palindrome
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # sliding window move right
        for i in range(len(s) - 1):
             result = max(result,
             expand(i ,i + 1), # for even palindrome
             expand(i, i + 2), # for odd palindrome
             key = len) # find the max length palindrome among those three words
        
        return result

# The key point is using two pointer.