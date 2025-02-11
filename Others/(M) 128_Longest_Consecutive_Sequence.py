from typing import List

"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        cons = 0

        for n in nums:
            if n - 1 not in nums:
                pos = n + 1
                while pos in nums:
                    pos += 1
                cons = max(cons, pos - n)

        return cons
