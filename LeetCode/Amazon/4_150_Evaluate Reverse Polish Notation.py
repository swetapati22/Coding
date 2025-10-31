#Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

##################### QUESTION #####################
# 150. Evaluate Reverse Polish Notation - Medium
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 
# Constraints:
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

##################### SOLUTION #####################
class Solution:
    """ 
        COMPANYs - AMAZON
        APPROACH:
        - Traverse the list and save the values of the list to a stack until an operator is found. List = (7,8,+,9,*) now stack has [7,8]
        - On finding an operator pop the top 2 values in order of their positioning in the initial list. 
            - That means the last poped value with will the 2nd value = 8, with interger typecasting
            - THe second last poped value is the 1st value = 7, with interger typecasting
        - Now the operator will be applied between (1st value = 7) OPERATOR (2nd value = 8) resulting in a solution value
        - Push this solution value will be pushed to the list and this process continues.
        - After complete traversal return the stack's only value.
            Time complexity: O(n)
            Space complexity: O(n)
    """
    def evalRPN(self, tokens: List[str]) -> int:
        store_stack = []
        for tok in tokens:
            if tok not in ("+", "-", "*", "/"):
                store_stack.append(int(tok))
            else:
                second_val = store_stack.pop()
                first_val = store_stack.pop()
                if tok == "+":
                    sol = first_val + second_val
                elif tok == "-":
                    sol = first_val - second_val
                elif tok == "*":
                    sol = first_val * second_val
                else:
                    sol = first_val / second_val
                store_stack.append(int(sol))
        return store_stack.pop()