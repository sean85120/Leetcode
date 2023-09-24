from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = nums[0]
        minp = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxp, minp = minp, maxp

            maxp = max(nums[i], maxp * nums[i])
            minp = min(nums[i], minp * nums[i])

            ans = max(ans, maxp)

        return ans
