from typing import List

# O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, j in enumerate(nums):

        print(f"index:{i} value:{j}")
        r = target - j
        if r in d:
            return [d[r], i]
        d[j] = i


nums = [2, 7, 11, 13]
target = 9
twoSum(nums, target)
