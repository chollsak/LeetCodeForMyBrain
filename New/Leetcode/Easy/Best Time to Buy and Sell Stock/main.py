from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to track the minimum price and maximum profit
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            print("minprice", min_price)
            
            # Calculate profit for the current price and update the maximum profit
            max_profit = max(max_profit, price - min_price)
            print("maxprofit", max_profit)
        
        return max_profit


# Example Usage
s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # Output should be 5
