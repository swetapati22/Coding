class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 1: HashMap Lookup (Optimal)
        - Idea: While iterating, store each number's index in a hash map.
        - For each number n at index i:
            1) Compute diff = target - n.
            2) If diff exists in the hash map, we found two indices -> return them.
            3) Otherwise, store n in the hash map with its index.
        - This guarantees finding the solution in one pass.

        Time Complexity: O(n)
            -> Each lookup (diff in hash map) and insertion is O(1) on average.
        Space Complexity: O(n)
            -> In the worst case, store all n numbers in the map.

        Alternate Approaches:

        2) Brute Force Double Loop (O(n^2), O(1) space)
           - Compare every pair (i, j) where i < j.
           - If nums[i] + nums[j] == target, return [i, j].
           - Steps:
             a) For i from 0 to n-1:
             b)   For j from i+1 to n-1:
             c)       Check if nums[i] + nums[j] == target.

        3) Sorting + Two Pointers (O(n log n) time, O(n) space)
           - Not typically used in LeetCode since we must return original indices,
             but possible with extra bookkeeping.
           - Steps:
             a) Pair each number with its index -> (num, idx).
             b) Sort by num.
             c) Use two pointers (left, right) to find a pair summing to target.
             d) Return original indices from stored pairs.
        """

        # Approach 1: HashMap Lookup (Optimal)
        findmap = {}  # number -> index
        for idx, n in enumerate(nums):
            diff = target - n  # complement needed
            if diff in findmap:  # found the pair
                return [findmap[diff], idx]
            findmap[n] = idx  # store current number with index


# ------------------------------
# Approach 2: Brute Force Double Loop
def twoSum_bruteforce(nums: List[int], target: int) -> List[int]:
    # Check all pairs (i, j)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# ------------------------------
# Approach 3: Sorting + Two Pointers
def twoSum_sorting(nums: List[int], target: int) -> List[int]:
    # Step 1: Pair numbers with their original indices
    nums_with_idx = [(num, idx) for idx, num in enumerate(nums)]

    # Step 2: Sort by the number value
    nums_with_idx.sort(key=lambda x: x[0])

    # Step 3: Use two pointers
    left, right = 0, len(nums_with_idx) - 1
    while left < right:
        total = nums_with_idx[left][0] + nums_with_idx[right][0]
        if total == target:
            return [nums_with_idx[left][1], nums_with_idx[right][1]]
        elif total < target:
            left += 1
        else:
            right -= 1
