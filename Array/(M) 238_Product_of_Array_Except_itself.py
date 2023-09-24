from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    product = 1
    zero_count = 0

    result = [1] * n

    for num in nums:
        if num == 0:
            zero_count += 1
            if zero_count > 1:
                return [0] * n
        else:
            product *= num

    if zero_count == 1:
        for i in range(n):
            if nums[i] == 0:
                result[i] = product
            else:
                result[i] = 0
    else:
        for i in range(n):
            result[i] = int(product / nums[i])

    return result
