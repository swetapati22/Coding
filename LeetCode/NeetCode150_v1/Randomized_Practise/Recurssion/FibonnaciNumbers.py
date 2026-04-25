"""
LeetCode Problem: 509. Fibonacci Number  
Level - Easy

The Fibonacci numbers, commonly denoted F(n), form a sequence such that each number is the sum of the two preceding ones, starting from 0 and 1:

F(0) = 0, F(1) = 1  
F(n) = F(n-1) + F(n-2), for n > 1

Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3

Constraints:
- 0 <= n <= 30
"""

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Recursive Approach
        if n <= 1:
            return n  # Base case: F(0) = 0, F(1) = 1
        
        lsum = self.fib(n-1)  # Compute F(n-1)
        hsum = self.fib(n-2)  # Compute F(n-2)

        fibb_sum = lsum + hsum  # F(n) = F(n-1) + F(n-2)

        return fibb_sum

    def fib_iterative(self, n):
        """
        Iterative Approach
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return 1

        prev1 = 0  # Represents F(0)
        prev2 = 1  # Represents F(1)

        for curr_num in range(2, n+1):
            curr_sum = prev1 + prev2
            prev1 = prev2
            prev2 = curr_sum

        return prev2  # Final Fibonacci number F(n)

# --- Approach (Recursive) ---
# 1. Use recursion to define F(n) = F(n-1) + F(n-2).
# 2. Base cases: F(0) = 0, F(1) = 1.

# --- Approach (Iterative) ---
# 1. Handle base cases separately (n = 0 or 1).
# 2. Use two variables to iteratively compute the Fibonacci sequence.
# 3. Update previous two values in each iteration.

# --- Time Complexity ---
# Recursive: O(2^N) – Exponential time due to repeated calculations.
# Iterative: O(N) – Linear time by building up from bottom.

# --- Space Complexity ---
# Recursive: O(N) – Call stack due to recursion depth.
# Iterative: O(1) – Constant space usage with just three variables.
