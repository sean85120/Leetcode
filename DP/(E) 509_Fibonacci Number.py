class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        dp_1 = 0
        dp_2 = 1
        for i in range(2, n + 1):
            di = dp_1 + dp_2

            dp_1 = dp_2
            dp_2 = di

        return di
