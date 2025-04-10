"""
LeetCode-Style Problem: Triplets with Smaller Sum  
Level - Medium

Given an array of unsorted numbers and a target sum, count all triplets such that:
arr[i] + arr[j] + arr[k] < target, where i < j < k.

Example 1:
Input: arr = [-1, 0, 2, 3], target = 3  
Output: 2  
Explanation: Triplets: [-1, 0, 2], [-1, 0, 3]

Example 2:
Input: arr = [-1, 4, 2, 1, 3], target = 5  
Output: 4  
Explanation: Triplets: [-1, 1, 2], [-1, 1, 3], [-1, 1, 4], [-1, 2, 3]

Constraints:
- The array can contain positive or negative integers
- i < j < k (no repeated indices)
"""

def triplet_with_smaller_sum(arr, target):
    arr.sort()                       # O(n log n) – Sort the array to enable two-pointer technique
    count = 0                        # O(1) – Initialize the result

    for i in range(len(arr) - 2):    # O(n) – Fix the first number of the triplet
        left = i + 1                 # O(1)
        right = len(arr) - 1         # O(1)

        while left < right:          # O(n) per i → total O(n^2)
            curr_sum = arr[i] + arr[left] + arr[right]  # O(1) – Sum of triplet

            if curr_sum < target:
                # Why use count += (right - left)?
                # Because the array is sorted, if arr[i] + arr[left] + arr[right] < target,
                # then ALL elements from left to right form valid triplets with arr[i]
                # E.g., arr[i] + arr[left] + arr[right-1] is also < target
                # So instead of counting each triplet individually, we count all of them at once.
                #
                # If we did count += 1 here, we’d undercount – we’d only count the current
                # triplet, and miss out on all other valid (left, right-1), (left, right-2)... pairs.
                count += right - left  # O(1) – Count all valid triplets in this window
                left += 1              # O(1) – Move left to explore new triplet base
            else:
                right -= 1             # O(1) – Sum is too large, try a smaller number

    return count                      # O(1)

# Time Complexity:
# - Sorting: O(n log n)
# - Outer loop: O(n)
# - Inner two-pointer loop: O(n) per i
# - Total Time Complexity: O(n^2)

# Space Complexity:
# - No extra data structures used
# - Auxiliary Space: O(1)