"""
LeetCode Problem: 3Sum Closest  
Level - Medium

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.  
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1  
Output: 2  
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

Example 2:
Input: nums = [0,0,0], target = 1  
Output: 0  
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0)

Example 3:
Input: nums = [-2, 0, 1, 2], target = 2  
Output: 1  
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Constraints:
- 3 <= nums.length <= 500
- -10^3 <= nums[i] <= 10^3
- -10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # O(n log n) – Sorting the array

        closest_sum = float('inf')  # O(1) – Initialize with an infinitely large value

        # Iterate through each element - O(n)
        for i in range(len(nums) - 2):
            left = i + 1  # O(1) – Start of the two-pointer range
            right = len(nums) - 1  # O(1) – End of the two-pointer range

            # Two-pointer loop - O(n) per i → overall O(n^2)
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]  # O(1) – Compute sum of triplet

                # If it's an exact match, return immediately
                if curr_sum == target:
                    return curr_sum  # O(1)

                # Update the closest_sum if:
                # - it's closer than the previous, OR
                # - it's equally close but smaller
                if (abs(curr_sum - target) < abs(closest_sum - target)) or \
                   (abs(curr_sum - target) == abs(closest_sum - target) and curr_sum < closest_sum):
                    closest_sum = curr_sum  # O(1)

                # Move pointers accordingly
                if curr_sum < target:
                    left += 1  # O(1)
                else:
                    right -= 1  # O(1)

        return closest_sum  # O(1)


# Time Complexity Analysis:
# - Sorting takes O(n log n)
# - Outer loop runs O(n) times
# - Inner two-pointer loop runs O(n) per outer iteration
# - Overall time complexity: **O(n^2)**

# Space Complexity:
# - No extra space used apart from variables
# - Sorting is in-place → **O(1)** auxiliary space
