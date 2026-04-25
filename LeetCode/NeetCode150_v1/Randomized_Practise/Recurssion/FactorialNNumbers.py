"""
LeetCode Problem: Factorial of a Given Number  
Level - Easy

You are given an integer n. Return the value of n! (n factorial).

The factorial of a number is the product of all positive integers less than or equal to that number.

Example 1:
Input: n = 2
Output: 2
Explanation: 2! = 1 * 2 = 2

Example 2:
Input: n = 0
Output: 1
Explanation: 0! is defined as 1

Constraints:
- 0 <= n <= 10^4
"""

class Solution:
    def factorial(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1  # Base case: 0! = 1 and 1! = 1

        return n * self.factorial(n-1)  # Recursive call multiplying n with factorial of (n-1)

# --- Approach ---
# Use recursion to calculate factorial:
# 1. Define the base case: if n is 0 or 1, return 1.
# 2. Otherwise, recursively return n multiplied by factorial of (n-1).
# 3. Use self.factorial(n-1) because we are calling a method inside a class.

# --- Time Complexity ---
# O(N) – We make a single recursive call for each number from N down to 1.

# --- Space Complexity ---
# O(N) – Due to the recursion call stack created for N recursive calls.
