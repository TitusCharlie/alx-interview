#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make up the total.

    Args:
        coins (List[int]): List of coin denominations.
        total (int): The target amount.

    Returns:
        int: The minimum number of coins needed, or -1 if it's not possible.
    """
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize the dp array with a large value (infinity-like)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make up 0 total

    # Iterate through each coin and update dp for all amounts
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it's not possible to make the total
    return dp[total] if dp[total] != float('inf') else -1