"""
LeetCode Problem: 75. Sort Colors  
Level - Medium

Given an array `nums` with `n` objects colored red (0), white (1), or blue (2), sort them **in-place** so that objects of the same color are adjacent, with the colors in the order: red, white, and blue.

You must solve this problem without using the library's sort function.

Example 1:
Input:  nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

Example 2:
Input:  nums = [2, 0, 1]
Output: [0, 1, 2]

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """

        low = 0                            # O(1) – pointer for 0 region
        mid = 0                            # O(1) – pointer for current element
        high = len(nums) - 1              # O(1) – pointer for 2 region

        while mid <= high:                # O(n) – single pass through array
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]  # O(1)
                mid += 1                                     # O(1)
                low += 1                                     # O(1)

            elif nums[mid] == 1:
                mid += 1                                     # O(1)

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]  # O(1)
                high -= 1                                       # O(1)

        return nums  # not necessary per problem, but harmless  # O(1)

# Time Complexity:
# - The algorithm scans the list once → O(n)
# - All operations inside the loop are O(1)
# - Overall time complexity is **O(n)**

# Space Complexity:
# - The algorithm uses only a few integer pointers → **O(1)** space
# - Sorting is done in-place