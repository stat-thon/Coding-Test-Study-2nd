# 파이썬 알고리즘 인터뷰 문제 07 - 두 수의 합
# https://leetcode.com/problems/two-sum
class Solution:
    # My solution
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
    # Solution
    def twoSum(self, nums, target):
        numMap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i