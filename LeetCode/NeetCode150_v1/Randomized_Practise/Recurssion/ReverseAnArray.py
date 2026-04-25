"""
LeetCode Problem: Reverse an Array (Using Recursion)  
Level - Easy

Given an array arr of n elements, reverse the array **in-place** using recursion.

Example 1:
Input: n = 5, arr = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Explanation: Reverse of [1, 2, 3, 4, 5] is [5, 4, 3, 2, 1]

Example 2:
Input: n = 6, arr = [1, 2, 1, 1, 5, 1]
Output: [1, 5, 1, 1, 2, 1]
Explanation: Reverse of [1, 2, 1, 1, 5, 1] is [1, 5, 1, 1, 2, 1]

Constraints:
- 1 <= n <= 10^5
- arr[i] is an integer
"""

class Solution:
    def reverse(self, arr, n):
        """
        :type arr: List[int]
        :type n: int
        :rtype: List[int]
        """

        def helper(left, right):
            if left >= right:
                return  # Base case: when pointers meet or cross

            arr[left], arr[right] = arr[right], arr[left]  # Swap
            helper(left + 1, right - 1)  # Recursive call moving inward

        helper(0, n - 1)
        return arr

# --- Approach ---
# Use recursion with two pointers (left and right):
# 1. Swap elements at 'left' and 'right'.
# 2. Move left pointer forward and right pointer backward.
# 3. Recursively call until left >= right.

# --- Time Complexity ---
# O(N) – Each element is involved in one swap.

# --- Space Complexity ---
# O(N) – Due to the recursion call stack.
