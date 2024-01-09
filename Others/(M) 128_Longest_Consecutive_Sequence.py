from typing import List


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
