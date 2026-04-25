class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        =========================
        Approach 1: Brute Force:
        =========================
        - For each element in the array check every other element in order to see if target is present.

            Time: O(n^2)
            Space: O(1)

        =========================
        Approach 2: Optimal
        =========================
        - Initution: Since the array is sorted and we have to search for something specific - we move ahead with the two pointer appraoch.
        - Start by left pointer at 0th position and right pointer at len(arr)-1 position.
        - We do the search till left pointer < right pointer.
        - Get the num of the left number + right number.
        - Decide which pointer to move:
            - if the current sum we have is > target: that means we have a bigger number and since array is sorted move the right pointer inside - so we are looking at a smaller number.
            - if the current sum is < target: that means we have a smaller number and since array is sorted move the left pointer forward.
            - if equal, return the index incremented by 1.
            Time: O(n)
            Space: O(1)
        """
        left = 0
        right = len(numbers)-1
        while right > left:
            cur_sum = numbers[left]+numbers[right]

            if cur_sum > target:
                right-=1
            elif cur_sum < target:
                left+=1
            else:
                return [left+1, right+1]