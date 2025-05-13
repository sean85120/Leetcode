from typing import List

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # add memo for reduce time complexity
        memo = dict()

        def dp(n):
            if n in memo:
                return memo[n]

            if n == 0:
                return 0
            if n < 0:
                return -1

            res = float("INF")

            for coin in coins:
                subproblem = dp(n - coin)

                # if subproblem is not solvable, skip
                if subproblem == -1:
                    continue

                res = min(res, subproblem + 1)

            # memoize the result after all coins are checked
            memo[n] = res if res != float("INF") else -1
            return memo[n]

        return dp(amount)
