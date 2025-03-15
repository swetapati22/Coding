"""
LeetCode Problem: 3Sum
Level - Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
- i != j, i != k, and j != k
- nums[i] + nums[j] + nums[k] == 0
The solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = [0,1,1]
Output: []

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the unique triplets such that their sum equals zero.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sorting takes O(n log n)
        triplets = []  # Initializing list takes O(1)
        
        # Iterate through the sorted array - O(n)
        for i in range(len(nums) - 2):
            # Skip duplicate elements to avoid redundant triplets - O(1) on average
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach starts - O(n) for each iteration of i
            target = -nums[i]  # O(1)
            left, right = i + 1, len(nums) - 1  # O(1)
            
            while left < right:  # O(n) in worst case
                curr_sum = nums[left] + nums[right]  # O(1)
                
                if curr_sum == target:
                    triplets.append([nums[i], nums[left], nums[right]])  # O(1)
                    left += 1  # O(1)
                    right -= 1  # O(1)
                    
                    # Skip duplicates for left pointer - O(n) in worst case
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for right pointer - O(n) in worst case
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum > target:
                    right -= 1  # O(1)
                else:
                    left += 1  # O(1)
        
        return triplets  # O(1)

# Time Complexity Analysis:
# - Sorting takes O(n log n)
# - Iterating through nums takes O(n)
# - Two-pointer search takes O(n) per iteration of i
# - Skipping duplicates is at most O(n) per iteration
# - Overall, the worst-case time complexity is **O(n^2)**, which is optimal compared to O(n^3) brute-force approaches.