"""
LeetCode Problem: Comparing Strings containing Backspaces  
Level - Medium

Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal after applying the backspaces.

Example 1:
Input: str1 = "xy#z", str2 = "xzz#"
Output: True
Explanation: After applying backspaces, both become "xz"

Example 2:
Input: str1 = "xy#z", str2 = "xyz#"
Output: False
Explanation: After applying backspaces, they become "xz" and "xy"

Example 3:
Input: str1 = "xp#", str2 = "xyz##"
Output: True
Explanation: Both reduce to "x"

Example 4:
Input: str1 = "xywrrmp", str2 = "xywrrmu#p"
Output: True
Explanation: Both remain "xywrrmp" after applying backspaces

Constraints:
- 1 <= len(str1), len(str2) <= 200
- str[i] can be lowercase letters or '#'
"""

class Solution(object):
    def backspaceCompare(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """

        def get_next_valid_index(s, index):
            """
            Helper to get the index of the next valid character,
            going backward while handling '#' as backspace.
            """
            backspace_count = 0
            while index >= 0:
                if s[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                index -= 1
            return index

        index1 = len(str1) - 1
        index2 = len(str2) - 1

        while index1 >= 0 or index2 >= 0:
            i1 = get_next_valid_index(str1, index1)
            i2 = get_next_valid_index(str2, index2)

            if i1 < 0 and i2 < 0:
                return True  # both strings fully processed

            if i1 < 0 or i2 < 0:
                return False  # one string is done before the other

            if str1[i1] != str2[i2]:
                return False  # mismatch found

            index1 = i1 - 1
            index2 = i2 - 1

        return True  # all characters matched

# --- Summary of Approach ---
# Use two pointers starting from the end of each string and skip characters using a helper function 
# that simulates the effect of backspaces. Compare the resulting characters step-by-step. 
# If any mismatch is found or leftover characters remain, return False. Otherwise, return True.

# --- Time Complexity ---
# O(M + N), where M and N are the lengths of str1 and str2

# --- Space Complexity ---
# O(1) – uses constant extra space (just counters and indices)
