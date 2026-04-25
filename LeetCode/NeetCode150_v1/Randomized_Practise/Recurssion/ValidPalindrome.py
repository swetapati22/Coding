"""
LeetCode Problem: 125. Valid Palindrome  
Level - Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 

Return True if the given string is a palindrome, otherwise return False.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: True
Explanation: Empty string is considered a valid palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome_recursive(self, s):
        """
        Recursive Approach
        :type s: str
        :rtype: bool
        """

        # Preprocess: Lowercase and remove non-alphanumeric characters
        s = ''.join(c.lower() for c in s if c.isalnum())

        def helper(left, right):
            if left >= right:
                return True  # Base case: pointers crossed
            if s[left] != s[right]:
                return False  # Mismatch found
            return helper(left + 1, right - 1)  # Move inward

        return helper(0, len(s) - 1)

    def isPalindrome_two_pointer(self, s):
        """
        Two Pointer Iterative Approach
        :type s: str
        :rtype: bool
        """

        # Preprocess: Lowercase and remove non-alphanumeric characters
        s = ''.join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False  # Mismatch found
            left += 1
            right -= 1

        return True  # All matched successfully

# --- Approach (Recursive) ---
# 1. Preprocess the string: remove non-alphanumeric characters and convert to lowercase.
# 2. Use recursion with two pointers (left and right):
#    - If characters match, continue inward.
#    - If characters mismatch, return False immediately.
# 3. Base case: pointers cross (left >= right), meaning it's a palindrome.

# --- Approach (Two-Pointer Iterative) ---
# 1. Preprocess the string similarly.
# 2. Use two pointers starting from the start and end.
# 3. Move the pointers toward each other, checking characters at each step.
# 4. If mismatch found, return False. If pointers cross without mismatch, return True.

# --- Time Complexity for Both Approaches ---
# O(N) – Preprocessing takes O(N), and comparing characters also takes O(N).

# --- Space Complexity ---
# Recursive Approach: O(N) – call stack in worst case.
# Iterative Two-Pointer Approach: O(1) extra space (after preprocessing).
