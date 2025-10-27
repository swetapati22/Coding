#Question: https://leetcode.com/problems/two-sum/

##################### QUESTION #####################
# 1. Two Sum - Easy
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

##################### SOLUTION #####################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
        COMPANYs - GOOGLE
        Approach1 (Bruteforce):
        - Check every combination with a particular element if they sum up to the targer.
        - Going through the entire array of length N - worst case
            Time complexity: O(n^2)
            Space complexity: O(1)

        Approach2 (Hashmap):
        - Hashmap:Value to Index and start target - curr_num and check if that exist if thr required number exisits in the hashmap.
        - If doesn't exisit then add the curr num to the hashmap.
            Time complexity: O(n) - Traversing the array once, then search in hashmap.
            Space complexity: O(n) - hashmap - worst case have to keep all elements in the hashmap
        """

        # Approach 1: Brute Force Double Loop
        def twoSum_bruteforce(nums: List[int], target: int) -> List[int]:
            # Check all pairs (i, j)
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
                    
        # Approach 2: HashMap Lookup (Optimal)
        findmap = {}  # number -> index
        for idx, n in enumerate(nums):
            diff = target - n  # complement needed
            if diff in findmap:  # found the pair
                return [findmap[diff], idx]
            findmap[n] = idx  # store current number with index