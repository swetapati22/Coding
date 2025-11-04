#Question: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
##################### QUESTION #####################
# 230. Kth Smallest Element in a BST - Medium
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 
# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104

##################### SOLUTION #####################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """ 
            COMPANYs - AMAZON
            APPROACH Recussion:
            - Inorder = left child, root, right (l+r)
            - Start from root, call recussion on left, till left exists.
            - Once curr.left is null, add curr_node to res.
            - Call recurssion on right,this becomes the new node and keep doing l+r
            - Repeat untill we reach end of the recurssion stack that is till we reach the root node back. 
            - Once the res is computed - by default:
                - FACT: Inorder traversal of BST is sorted. 
            - So just pick the kth element - array starts from 0 so pick k-1
            - Return result
                Time complexity: O(n)
                Space complexity: O(n)  
        """
        res = []

        def inorder(curr_node):
            if not curr_node:
                return
            inorder(curr_node.left)
            res.append(curr_node.val)
            inorder(curr_node.right)

        inorder(root)
    
        return res[k-1]
        
        

        