from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0:
                if v == nums[i - 1]:
                    return True
        return False
