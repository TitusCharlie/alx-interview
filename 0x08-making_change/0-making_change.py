#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (List[int]): List of coin denominations.
        total (int): Target amount to achieve.

    Returns:
        int: Fewest number of coins needed, or -1 if total cannot be achieved.
    """
    if total <= 0:
        return 0

    # Initialize the DP array with a large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins needed to make total 0

    # Fill the DP table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if the total can be achieved
    return dp[total] if dp[total] != float('inf') else -1