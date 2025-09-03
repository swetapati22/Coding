class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach:
        - First check if lengths differ; if yes, return False immediately (not an anagram).
        - Use two hash maps (dictionaries) to count the frequency of each character in both strings.
        - Iterate through each index, update the character counts for both strings.
        - Finally, compare both dictionaries; if counts differ for any character, return False.
        - Otherwise, return True.

        Time Complexity: O(n)
            - We iterate through the strings once (n = len(s) = len(t)).
            - Dictionary lookups and updates are O(1) on average.
        Space Complexity: O(1)
            - In the worst case, we store counts for all 26 lowercase English letters.
            - So effectively constant space relative to input size.
            - (If Unicode characters were allowed, space complexity would be O(k), where k = number of unique characters.)
        """

        # Step 1: Quick length check
        if len(s) != len(t):
            return False

        # Step 2: Create dictionaries to count frequency of characters
        countS, countT = {}, {}

        # Step 3: Count characters in both strings
        for i in range(len(s)):
            curr_s = s[i]
            curr_t = t[i]

            countS[curr_s] = countS.get(curr_s, 0) + 1
            countT[curr_t] = countT.get(curr_t, 0) + 1

        # Step 4: Compare both frequency maps
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        # Step 5: If all counts match, strings are anagrams
        return True
