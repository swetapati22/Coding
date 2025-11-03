#Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

##################### QUESTION #####################
# 121. Best Time to Buy and Sell Stock - Easy
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

##################### SOLUTION #####################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        COMPANYs - AMAZON, GOOGLE
        Approach1:
        - Think of this like a time series data where the order of data based on the time matters.
        - So keep moving forward in time with the help of two pointers, left and right.
        - Traverse left pointer from 0th index and right from 1st index, till array end.
        - Goal: find ideal time to buy when the stock price is at minimum, and sell when stock price is maximum.
            - When left price is less than right price, that means profit is positive - keep updating max_value variable (calculate sell - buy to get profit).
            - If contradicted, move left pointer to the position of the right pointer as that is the current lowest price to buy, and move right point one place forward.
            - Irespective of left price < right price or not, right keeps moving to compare each day's price with the current lowest (left pointer). 
        - Return max_value variable when you complete array traversal.
            Time complexity: O(n) - Visit each element until r finishes array traversal.
            Space complexity: O(1) - Using two pointers and max_profits variable.
        """
        left = 0
        max_profit = float("-inf") #prices = [7,1,5,3,6,4] left = 1, right = 3
        for right in range(1,len(prices)):
            if prices[left] > prices[right]:
                left = right
                right +=1
                continue
            max_profit = max(prices[right]-prices[left], max_profit) #4
            right +=1
        return max_profit if max_profit!= float("-inf") else 0