"""
LeetCode Problem: Two Sum
Level - Easy 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store numbers and their corresponding indices - O(1) per insertion
        nums_to_index = {} 
        
        # Iterate through the list - O(n)
        for idx, num in enumerate(nums):
            # Calculate the complement value needed to reach target - O(1)
            complement = target - num
            
            # Check if the complement is already in the dictionary - O(1) lookup
            if complement in nums_to_index:
                return [idx, nums_to_index[complement]]  # O(1) return operation
            
            # Store the current number and its index in the dictionary - O(1) insertion
            nums_to_index[num] = idx
        
        # If no solution is found (though the problem guarantees one exists) - O(1)
        return []

# Time Complexity Analysis:
# - Iterating through the list: O(n)
# - Dictionary lookup (checking complement existence): O(1) per operation
# - Dictionary insertion: O(1) per operation
# - Overall time complexity: **O(n)**, which is optimal compared to O(n^2) brute-force approaches.