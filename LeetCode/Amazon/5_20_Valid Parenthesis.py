#Question: https://leetcode.com/problems/valid-parentheses/description/

##################### QUESTION #####################
# 20. Valid Parentheses - Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
##################### SOLUTION #####################
class Solution:
    """ 
        COMPANYs - AMAZON
        APPROACH:
        - Traverse the list and initialize a stack.
        - Check if you get the closing parenthesis - is the top of the stack a open parenthesis (have individual checks for all 3 parenthesis types).
            - If yes, continue
        - If you don't find an open parenthesis for the closing one - then push it to the stack.
        - If you end up traversing till the end of the string and something still remains in the stack then return False.
        - If after complete traversal - stack is empty - return True.
            Time complexity: O(n)
            Space complexity: O(n)
    """
    def isValid(self, s: str) -> bool:
        all_parenthesis = []
        for par in s:
            if all_parenthesis and par == ")" and all_parenthesis.pop() == "(":
                continue
            elif all_parenthesis and par == "]" and all_parenthesis.pop() == "[":
                continue
            elif all_parenthesis and par == "}" and all_parenthesis.pop() == "{":
                continue
            else:
                all_parenthesis.append(par)
        
        if all_parenthesis:
            return False
        
        return True