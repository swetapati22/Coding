class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach 1: HashSet (Optimal)
        Use a HashSet to track numbers seen so far while iterating over the list.
        - For each number in nums:
            - If it is already in the set, return True (duplicate found).
            - Otherwise, add it to the set.
        - If the loop finishes without finding duplicates, return False.

        Time Complexity: O(n) 
            -> Each membership check and insertion into the set takes O(1) on average.
        Space Complexity: O(n) 
            -> In the worst case (all unique numbers), the set stores n elements.

        Alternate Approaches:

        2) Brute Force Pairwise Check
           - Compare every element with every other element.
           - Time Complexity: O(n^2), Space Complexity: O(1)

        3) Sort Then Linear Scan
           - Sort the array; duplicates will become adjacent.
           - Then scan once and check if nums[i] == nums[i+1].
           - Time Complexity: O(n log n), Space Complexity: O(1) if sorted in place,
             O(n) if sorting a copy.
        """

        # Approach 1: HashSet (Optimal)
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False


# ------------------------------
# Approach 2: Brute Force O(n^2)
def containsDuplicate_bruteforce(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# ------------------------------
# Approach 3: Sort + Linear Scan O(n log n)
def containsDuplicate_sorting(nums: List[int]) -> bool:
    nums.sort()  # modifies list in place
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
