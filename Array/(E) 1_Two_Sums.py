from typing import List

"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):

            print(f"index:{i} value:{j}")
            r = target - j
            if r in d:
                return [d[r], i]
            d[j] = i


nums = [2, 7, 11, 13]
target = 9
print(Solution().twoSum(nums, target))
