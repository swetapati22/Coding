#Question: https://leetcode.com/problems/longest-palindromic-substring/description/

##################### QUESTION #####################
# 5. Longest Palindromic Substring - Medium
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

##################### SOLUTION #####################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ 
        COMPANYs - AMAZON, GOOGLE
        Approach (Brute Force):
        - Two for loops, to check starting from each character.
        - Now slice the string iterating through the next characters till we reach the end of the string.
        - Check that string with its reverse to check for palindrome, if yes update the max_length of this combination and update the result.
        - Keep doing untill we complete checking all combination.
            Time complexity: O(n^3)
            Space complexity: O(n) - Each check creates temporary slices of size up to O(k) (where k is substring length) - worst case complete string

        Approach (Optimal):
        - Traverse the string and expand 2 pointers in the opposit direction from the current character.
        - Iterate through left and right movements, if equal from that current character moving outwards, else break.
        - Keep a global max substring length and at each outward movement, compare current length with global max length and update substring.
        - Edge case - odd and even palindrome check:
            - Start the left and right characters from the same character that would ensure the odd case satisfies
            - Start the left and right characters from current and next character to check for even case.
        - Repeat the same process for odd and even cases as we won't get to know before hand which case applies.
            Time complexity: O(n^2)
            Space complexity: O(1)
        """
        #Approach (Brute Force):
        res = ""
        max_len = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if (j-i+1) > max_len:
                        max_len = j-i+1
                        res = s[i:j+1]
        return res

        #Approach (Optimal):
        res = ""
        max_len = 0
        for i in range(len(s)):
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    res=s[l:r+1]
                    max_len = r-l+1
                l , r = l-1, r+1
            
            l, r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    res=s[l:r+1]
                    max_len = r-l+1
                l , r = l-1, r+1    
        return res

        