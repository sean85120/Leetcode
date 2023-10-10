from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        def int_to_binary(n) -> str:
            bits = 0

            while n != 0:
                if n % 2 == 1:
                    bits += 1
                n = n // 2

            return bits

        for i in range(n + 1):
            bits = int_to_binary(i)
            result.append(bits)

        return result
