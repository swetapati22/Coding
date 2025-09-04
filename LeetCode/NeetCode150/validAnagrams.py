class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach 1: HashMap Counting (Optimal)
        - Idea: Count the frequency of each character in both strings and compare.
        - Steps:
            1) If lengths differ, return False immediately (different sizes can't be anagrams).
            2) Initialize two dicts: smap for s and tmap for t (char -> count).
            3) Single pass over indices:
               - Increment smap[s[i]]
               - Increment tmap[t[i]]
            4) Iterate over keys in smap and verify smap[c] == tmap.get(c, 0).
            5) If all counts match, return True; else False.

        Time Complexity: O(n)
            -> One pass to build counts + one pass to compare.
            -> Dict get/update are O(1) on average.
        Space Complexity: O(1) for lowercase English letters (bounded by 26),
            O(k) in general where k = number of distinct characters.

        Alternate Approaches:

        2) Sorting & Compare (O(n log n), O(n) space)
           - Idea: Sorting brings equal characters together in the same order for anagrams.
           - Steps:
             a) (Optional) If lengths differ, return False.
             b) Compute s_sorted = sorted(s) and t_sorted = sorted(t).
             c) Return True iff s_sorted == t_sorted (exact same sequence of characters).

        3) Sorting & Character-by-Character (O(n log n), O(n) space)
           - Idea: Same as (2), but do an explicit linear scan to detect the first mismatch.
           - Steps:
             a) If lengths differ, return False.
             b) Sort both: s_sorted = sorted(s), t_sorted = sorted(t).
             c) For i from 0 to n-1:
                - If s_sorted[i] != t_sorted[i], return False (mismatch).
             d) If loop completes, return True.

        4) Counter from collections (O(n), O(1) space for lowercase letters; O(k) general)
           - Idea: Use Python’s Counter to build frequency maps succinctly.
           - Steps:
             a) (Optional) If lengths differ, return False.
             b) Build counters: Counter(s) and Counter(t).
             c) Return True iff the two Counter objects are equal.
           - Note: Naturally handles Unicode; for case-insensitive or Unicode-normalized
             comparisons, normalize/casefold before counting.
        """

        # Approach 1: HashMap Counting (Optimal)

        # Step 1: If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Create two dictionaries to store char -> frequency
        smap, tmap = {}, {}

        # Step 3: Count frequencies of each character in both strings
        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i], 0) + 1  # increment count for s[i] in smap
            tmap[t[i]] = tmap.get(t[i], 0) + 1  # increment count for t[i] in tmap

        # Step 4: Compare the two frequency dictionaries
        for c in smap:
            if smap[c] != tmap.get(c, 0):  # check if counts match
                return False

        # Step 5: If all counts match, the strings are anagrams
        return True


# ------------------------------
# Approach 2: Sorting & Compare
def isAnagram_sorting(s: str, t: str) -> bool:
    # Sort both strings and directly compare equality
    return sorted(s) == sorted(t)


# ------------------------------
# Approach 3: Sorting & Character-by-Character
def isAnagram_sorting_charwise(s: str, t: str) -> bool:
    # Step 1: Quick check on lengths
    if len(s) != len(t):
        return False

    # Step 2: Sort both strings
    s_sorted, t_sorted = sorted(s), sorted(t)

    # Step 3: Compare characters one by one
    for i in range(len(s_sorted)):
        if s_sorted[i] != t_sorted[i]:
            return False

    # Step 4: If no mismatch, return True
    return True


# ------------------------------
# Approach 4: Counter (Optimal & Concise)
from collections import Counter
def isAnagram_counter(s: str, t: str) -> bool:
    # Build counters for both strings and check equality
    return Counter(s) == Counter(t)
