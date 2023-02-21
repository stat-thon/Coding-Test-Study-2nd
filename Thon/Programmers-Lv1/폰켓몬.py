from collections import Counter
def solution(nums):
    return min(len(Counter(nums)), len(nums) // 2)