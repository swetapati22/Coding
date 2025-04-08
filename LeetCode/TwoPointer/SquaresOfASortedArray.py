"""
LeetCode Problem: Squares of a Sorted Array  
Level - Easy

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]  
Output: [0,1,9,16,100]

Example 2:
Input: nums = [-7,-3,2,3,11]  
Output: [4,9,9,49,121]

Constraints:
- 1 <= nums.length <= 10⁴
- -10⁴ <= nums[i] <= 10⁴
- nums is sorted in non-decreasing order
"""

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)                    # O(1)
        result = [0] * n                 # O(n) – allocate output array
        left, right = 0, n - 1           # O(1)
        highest_idx = n - 1              # O(1)

        while left <= right:             # O(n)
            left_sq = nums[left] ** 2    # O(1)
            right_sq = nums[right] ** 2  # O(1)

            if left_sq > right_sq:       # O(1)
                result[highest_idx] = left_sq  # O(1)
                left += 1                      # O(1)
            else:
                result[highest_idx] = right_sq  # O(1)
                right -= 1                      # O(1)

            highest_idx -= 1             # O(1)

        return result                    # O(1)

# Time Complexity Analysis:
# - We iterate over the array once → O(n)
# - All operations inside the loop are constant → O(1)
# - Overall time complexity is **O(n)**

# Space Complexity:
# - We use a result array of the same size → **O(n)**
# - If modifying in-place was allowed, it could be optimized to O(1)
