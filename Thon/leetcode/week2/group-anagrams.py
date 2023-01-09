# 파이썬 알고리즘 인터뷰 6장 5번 문제
# https://leetcode.com/problems/group-anagrams/

class Solution:
    # My solution
    def groupAnagrams(self, strs):
        from collections import defaultdict
        anagram_dict = defaultdict(list)
        
        for word in strs:
            used_letter = tuple(sorted(letter for letter in word))
            anagram_dict[used_letter].append(word)
        
        return anagram_dict.values()
    
    # Solution
    def solution(self, strs):
        import collections
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())
        # Solution is almost same with my solution.
        # The only difference is it sorted string itself -> it became a list
        # and then use join to make it string -> it became a string and used it as a key
        # But i used tuple as a key. That's the only difference