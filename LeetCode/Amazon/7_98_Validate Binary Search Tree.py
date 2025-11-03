#Question: https://leetcode.com/problems/validate-binary-search-tree/description/

##################### QUESTION #####################
# 98. Validate Binary Search Tree - Medium
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

##################### SOLUTION #####################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """ 
        COMPANYs - AMAZON
        Approach:
        - To validate BST, I will traverse each node from the root - I have to check left and right both:
            - Each time I check left child this becomes my current_node:
                - Take parent's left limit and Conditon to check will be -> parent's left limit < current_node and curr_root < parent value.
            - Similarly each time I check right child this becomes my current_node:
                - Take parent's right limit and Conditon to check will be -> parent value < current_node and curr_root < parent's right limit.
            -  While starting this recurssion - pass parent's left as -inf and parent's right as +inf
        - Going through the entire array of length N
            Time complexity: O(n)
            Space complexity: O(n)
        """
        def valid(root, left, right):
            if not root:
                return True
            if not (left<root.val and root.val<right): 
                return False
                # if the condition inside the bracket becomes true then should be correct so if not true then I should return False
            return (valid(root.left, left, root.val) and valid (root.right, root.val, right)) 
        return valid(root, float("-inf"), float("inf"))