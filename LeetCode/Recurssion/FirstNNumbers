"""
LeetCode Problem: Sum of First N Numbers  
Level - Easy

Given an integer N, return the sum of the first N natural numbers. Solve this using recursion.

Example 1:
Input: N = 4
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10

Example 2:
Input: N = 2
Output: 3
Explanation: 1 + 2 = 3

Constraints:
- 0 <= N <= 10^4
"""

class Solution:
    def NnumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0  # Base case: Sum of 0 numbers is 0
        
        return N + self.NnumbersSum(N-1)  # Recursive call

# --- Approach ---
# Use recursion to solve the problem:
# 1. Define a base case: if N == 0, return 0.
# 2. Otherwise, return N + sum of the first (N-1) numbers by making a recursive call.
# 3. Use self.NnumbersSum(N-1) because we are calling a method inside a class.

# --- Time Complexity ---
# O(N) – We make a single recursive call for each number from N down to 0.

# --- Space Complexity ---
# O(N) – Due to the recursion call stack created for N recursive calls.
