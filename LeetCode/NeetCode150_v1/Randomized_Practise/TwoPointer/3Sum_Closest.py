"""
LeetCode Problem: 3Sum Closest  
Level - Medium

Given an integer array `nums` of length n and an integer `target`, find three integers in `nums` such that the sum is **closest** to `target`.

Return the **sum of the three integers**.  
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1, 2, 1, -4], target = 1  
Output: 2  
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

Example 2:
Input: nums = [0, 0, 0], target = 1  
Output: 0  
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0)

Constraints:
- 3 <= nums.length <= 500  
- -10³ <= nums[i] <= 10³  
- -10⁴ <= target <= 10⁴
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()                                # O(n log n) – sort input array

        closest_sum = float('inf')                 # O(1) – initialize result variable

        for i in range(len(nums)):                 # O(n) – loop through array to fix the first element
            left = i + 1                            # O(1)
            right = len(nums) - 1                   # O(1)

            while left < right:                    # O(n) per iteration → total O(n^2)
                curr_sum = nums[i] + nums[left] + nums[right]  # O(1)

                if curr_sum == target:             # O(1)
                    return curr_sum                # O(1)

                # Update closest sum if better or equally close but smaller
                if (
                    abs(curr_sum - target) < abs(closest_sum - target) or         # O(1)
                    (abs(curr_sum - target) == abs(closest_sum - target) and      # O(1)
                     curr_sum < closest_sum)                                      # O(1)
                ):
                    closest_sum = curr_sum         # O(1)

                if curr_sum < target:
                    left += 1                      # O(1)
                else:
                    right -= 1                     # O(1)

        return closest_sum                         # O(1)

# Time Complexity Analysis:
# - Sorting the array: O(n log n)
# - Outer loop to fix the first element: O(n)
# - Inner two-pointer loop: O(n) per outer → O(n^2) total
# - Overall time complexity is **O(n^2)**

# Space Complexity:
# - Only a few pointers and variables are used → **O(1)** space
# - No extra data structures needed
