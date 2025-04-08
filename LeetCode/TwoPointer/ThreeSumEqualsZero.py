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
        triplet = []  # O(1) – initializing result list

        nums.sort()  # O(n log n) – sorting the array

        for start_ptr_idx, start_ptr in enumerate(nums):  # O(n) – loop through each element
            target = -start_ptr  # O(1) – simple negation

            # Skip duplicates for the starting element
            if start_ptr_idx != 0 and nums[start_ptr_idx] == nums[start_ptr_idx - 1]:
                continue  # O(1) – skip logic

            left_ptr = start_ptr_idx + 1  # O(1) – init left pointer
            right_ptr = len(nums) - 1     # O(1) – init right pointer

            while left_ptr < right_ptr:  # O(n) per start_ptr -> total O(n^2)
                curr_sum = nums[left_ptr] + nums[right_ptr]  # O(1) – compute sum

                if curr_sum == target:
                    triplet.append([nums[start_ptr_idx], nums[left_ptr], nums[right_ptr]])  # O(1) – append result
                    left_ptr += 1  # O(1)
                    right_ptr -= 1  # O(1)

                    # Skip duplicates for left pointer
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr - 1]:
                        left_ptr += 1  # O(n) in worst case (if many duplicates)

                    # Skip duplicates for right pointer
                    while left_ptr < right_ptr and nums[right_ptr] == nums[right_ptr + 1]:
                        right_ptr -= 1  # O(n) in worst case (if many duplicates)

                elif curr_sum < target:
                    left_ptr += 1  # O(1)
                else:
                    right_ptr -= 1  # O(1)

        return triplet  # O(1)


# Time Complexity:
# - Sorting takes O(n log n)
# - Iterating through nums takes O(n)
# - Two-pointer search takes O(n) per iteration of i
# - Skipping duplicates is at most O(n) per iteration
# - Overall, the worst-case time complexity is **O(n^2)**, which is optimal compared to O(n^3) brute-force approaches.

# Space Complexity:
# - Output list only → **O(1)** auxiliary space (excluding result)