# Function to find the number of
# vowel permutations possible
def countVowelPermutation(n):

    # To avoid the large output value
    MOD = 1e9 + 7

    # Initialize 2D dp array
    dp = [[0 for i in range(5)] for j in range(n + 1)]

    # Initialize dp[1][i] as 1 since
    # string of length 1 will consist
    # of only one vowel in the string
    for i in range(5):
        dp[1][i] = 1

    # Directed graph using the
    # adjacency matrix
    relation = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]

    # Iterate over the range [1, N]
    for i in range(1, n, 1):

        # Traverse the directed graph
        for u in range(5):
            dp[i + 1][u] = 0

            # Traversing the list
            for v in relation[u]:

                # Update dp[i + 1][u]
                dp[i + 1][u] += dp[i][v] % MOD

    # Stores total count of permutations
    ans = 0
    for i in range(5):
        ans = (ans + dp[n][i]) % MOD

    # Return count of permutations
    return int(ans)


# Driver code
if __name__ == "__main__":
    N = 2
    print(countVowelPermutation(N))
