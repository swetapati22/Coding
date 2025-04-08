"""
LeetCode Problem: Remove Duplicates from Sorted Array  
Level - Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.

After removing the duplicates, return the number of unique elements (let's call it `k`). Modify the input array `nums` such that the first `k` elements contain the unique values in the same relative order.  
The rest of the array beyond index `k - 1` does not matter.

Example 1:
Input: nums = [1,1,2]  
Output: 2, nums = [1,2,_]  
Explanation: The first two elements are 1 and 2. The rest can be anything.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]  
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
- 1 <= nums.length <= 3 * 10⁴  
- -100 <= nums[i] <= 100  
- nums is sorted in non-decreasing order
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # O(1)

        write_pointer = 1  # O(1) – First unique element is already in place

        for read_pointer in range(1, len(nums)):  # O(n)
            if nums[read_pointer] != nums[read_pointer - 1]:  # O(1)
                nums[write_pointer] = nums[read_pointer]  # O(1)
                write_pointer += 1  # O(1)

        return write_pointer  # O(1)


# Time Complexity Analysis:
# - We iterate through the array once → O(n)
# - All operations inside the loop are constant time → O(1)
# - Overall time complexity is **O(n)**

# Space Complexity:
# - In-place solution → no extra space used
# - Overall space complexity is **O(1)**
