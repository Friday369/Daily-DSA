# BRUTE FORCE
# Time: O(n²)  Space: O(1)
def maxProfit_brute():
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    print(f"Brute Force Result: {max_profit}")

maxProfit_brute()