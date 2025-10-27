#Question: https://leetcode.com/problems/longest-palindrome/

##################### QUESTION #####################
# 409. Longest Palindrome - Easy
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

##################### SOLUTION #####################
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """ 
        COMPANYs - AMAZON
        Approach1 (Hashmap):
        - Traverse the string and store freq in hashmap, if freq of curr_ch is even then increment result to 2, if odd then nothing.
        - This ensure we took all the possible combinations that can create the palindrome.
        - If there are odd occurances - they can go in the middle of the palindrome and then we increment result + 1 if any one of the characters exist in odd number.
            Time complexity: O(n)
            Space complexity: O(1) -> O(52) - 26 lower + 26 upper

        Approach2 (Hashset):
        - Traverse the string, if exist in set then increment res + 2, if doesn't exist in set then add to set.
        - After complete string traversal, if set is not empty then increment res + 1
        - Return result
            Time complexity: O(n)
            Space complexity: O(1) -> O(52) - 26 lower + 26 upper
        """

        #Approach1 (Hashmap):
        res = 0 
        freq_map = {}
        for ch in s:
            freq_map[ch] = freq_map.get(ch,0)+1
            if freq_map[ch]%2 == 0:
                res+=2

        if len([i for i in freq_map.values() if i%2!=0]):
            res+=1

        return res


        #Approach2 (Hashset):
        res = 0 
        freq_set = set()
        for ch in s:
            if ch in freq_set:
                freq_set.remove(ch)
                res+=2
            else:
                freq_set.add(ch)

        return res+1 if freq_set else res



        
        