"""
LeetCode Problem: Quadruple Sum to Target  
Level - Medium

Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example 1:
Input: nums = [4, 1, 2, -1, 1, -3], target = 1
Output: [[-3, -1, 1, 4], [-3, 1, 1, 2]]

Example 2:
Input: nums = [2, 0, -1, 1, -2, 2], target = 2
Output: [[-2, 0, 2, 2], [-1, 0, 1, 2]]

Constraints:
- 4 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()                        # O(n log n) – sort the array first
        n = len(nums)                      # O(1)
        result = []                        # O(1)

        for i in range(n - 3):             # O(n) – fix first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue                   # Skip duplicate for i

            for j in range(i + 1, n - 2):  # O(n) – fix second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue               # Skip duplicate for j

                left, right = j + 1, n - 1

                while left < right:        # O(n) – two-pointer for remaining two numbers
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])  # O(1)
                        left += 1
                        right -= 1

                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1          # Move left to increase sum
                    else:
                        right -= 1         # Move right to decrease sum

        return result                      # O(1)

# --- Approach ---
# 1. Sort the array to apply two-pointer technique and handle duplicates.
# 2. Use two nested loops to fix the first two numbers (i and j).
# 3. For the remaining two numbers, apply two-pointer (left and right) strategy.
# 4. Skip duplicates at every level to ensure only unique quadruplets are included.

# Time Complexity:
# - Sorting takes O(n log n)
# - Two nested loops take O(n^2)
# - Two-pointer inside takes O(n)
# - Overall: O(n^3)

# Space Complexity:
# - Sorting is in-place if allowed → O(1)
# - Output list depends on number of results → O(k), where k = number of valid quadruplets
