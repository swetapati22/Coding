class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach:
        Use a HashSet to track numbers seen so far while iterating over the list.
        - For each number in nums:
            - If it is already in the set, return True (duplicate found).
            - Otherwise, add it to the set.
        - If the loop finishes without finding duplicates, return False.

        Time Complexity: O(n) 
            -> Each membership check and insertion into the set takes O(1) on average.
        Space Complexity: O(n) 
            -> In the worst case (all unique numbers), the set stores n elements.
        """

        # Initialize an empty set to store unique numbers we encounter
        hashset = set()

        # Traverse through the entire list of numbers
        for i in range(len(nums)):
            # If the current number is already in the set,
            # that means we've seen it before -> duplicate found
            if nums[i] in hashset:
                return True

            # Otherwise, add the number to the set for future tracking
            hashset.add(nums[i])

        # If no duplicates were found after checking all elements, return False
        return False
