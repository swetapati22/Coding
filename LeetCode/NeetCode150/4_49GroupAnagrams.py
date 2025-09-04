from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach 1: Character-Count Signature (Optimal for lowercase a–z)
        - Idea: Two strings are anagrams iff they have the same frequency for each letter.
        - Steps:
            1) For each string s, build a length-26 array cnt where cnt[i] is the
               frequency of chr(ord('a') + i) in s.
            2) Use the tuple(cnt) as a hashable signature key in a map: key -> list of anagrams.
            3) Append s to its bucket.
            4) Return the buckets (map values).

        Time Complexity: O(N * K)
            -> N = number of strings, K = average length of each string.
            -> For each string, we count characters in O(K).
        Space Complexity: O(N * K)
            -> We store all input strings across the grouped lists.
            -> Each key is a 26-int tuple (constant size).

        Alternate Approaches:

        2) Sorting Signature (O(N * K log K), O(N * K) space)
           - Idea: Sort each string; anagrams share the same sorted form.
           - Steps:
             a) key = ''.join(sorted(s)) for each s
             b) group by key in a map, return the grouped values.

        3) Brute Force Pairing (O(N^2 * K), O(N) space)
           - Idea: For each string, scan remaining strings to see which are anagrams (via counting).
           - Steps:
             a) For each string i, compare with j > i.
             b) If they are anagrams, put them in the same group.
             c) Keep track of visited strings to avoid regrouping.
        """

        # Approach 1: Character-Count Signature (Optimal)
        res_map = defaultdict(list)             # dictionary: signature -> list of anagrams
        for s in strs:
            cnt = [0] * 26                      # frequency array for 'a'..'z'
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1    # increment the count for this character
            res_map[tuple(cnt)].append(s)       # use tuple(cnt) as key, append word to group

        # Convert grouped anagrams to list of lists and return
        return list(res_map.values())


# ------------------------------
# Approach 2: Sorting Signature (O(N * K log K))
def groupAnagrams_sorting(strs: List[str]) -> List[List[str]]:
    """
    Sort each string to form a key; anagrams share the same sorted string.
    Time: O(N * K log K) due to sorting each string.
    Space: O(N * K) to store groups and keys.
    """
    groups = defaultdict(list)                  # sorted_string -> list of anagrams
    for s in strs:
        key = ''.join(sorted(s))                # sorting brings same letters together
        groups[key].append(s)                   # group strings with the same sorted key
    return list(groups.values())


# ------------------------------
# Approach 3: Brute Force Pairing (O(N^2 * K))
def groupAnagrams_bruteforce(strs: List[str]) -> List[List[str]]:
    """
    Compare each string with the rest and bucket anagrams together.
    Time: O(N^2 * K) if using counting comparison per pair.
    Space: O(N) for grouping and a visited set.
    """
    def is_anagram(a: str, b: str) -> bool:
        # Quick length check
        if len(a) != len(b):
            return False

        # Count characters in a
        count = [0] * 26
        for ch in a:
            count[ord(ch) - ord('a')] += 1

        # Subtract counts for b
        for ch in b:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:                  # mismatch if count goes negative
                return False

        return True                             # counts matched → anagram

    res, visited = [], [False] * len(strs)      # result list and visited tracker
    for i in range(len(strs)):
        if visited[i]:                          # skip if already grouped
            continue
        group = [strs[i]]                       # start a new group
        visited[i] = True
        for j in range(i + 1, len(strs)):
            if not visited[j] and is_anagram(strs[i], strs[j]):
                group.append(strs[j])           # add to group if anagram
                visited[j] = True               # mark as used
        res.append(group)                       # add group to results
    return res
