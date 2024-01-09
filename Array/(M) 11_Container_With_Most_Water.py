from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1

        max_result = 0

        while l < r:
            current_area = min(height[l], height[r]) * (r - l)
            max_result = max(max_result, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_result
