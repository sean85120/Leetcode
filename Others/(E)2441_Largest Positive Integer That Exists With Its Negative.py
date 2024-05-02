from typing import List


# O(n log n), beacuse sorting a list takes O(n log n) time
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] > 0 and -nums[i] in nums:
                return nums[i]
        return -1  # If no such pair found


# O(n log n), first try, but not optimal
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        cur_max = 0
        neg_int = []
        for i in sort_nums:
            if i < 0:
                neg_int.append(i)

            if i > 0:
                if -i in neg_int:
                    cur_max = i
        return cur_max if cur_max != 0 else -1
