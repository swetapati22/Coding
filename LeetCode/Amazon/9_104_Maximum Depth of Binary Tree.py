#Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/
##################### QUESTION #####################
# 104. Maximum Depth of Binary Tree - Easy
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2
 
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

##################### SOLUTION #####################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ 
            COMPANYs - AMAZON
            1. APPROACH (Recussive DFS):
            - Base case = if root is null return 0 (nothing is there so no depth)
            - If root is not null: 
                - Always consider root to be of height 1, and recursively keep checking which child has more height, so take the child with max height.
                - Keep recursively checking the same for each child untill you reach the root in the recursion stack.
            - Return result
                Time complexity: O(n)
                Space complexity: O(n)  

            2. APPROACH (Recussive BFS - Level Order Traversal):
            - Base case = if root is null return 0 (nothing is there so no depth)
            - If root is not null: 
            - Maintain a dqueue, insert nodes to the same, start with root for level 0:
            - Keeping checking for right and left child of nodes at current level (while q).
                - Capture a current snapshot of q or length of q to keep track of the length: for i in len q:
                    - For each i, pop i (all current level nodes)
                    - Insert their respective left and right children.
                - Once the current length exhausted then increase the level and move to the next level to capture the next level's snapshot.
            - Return result
                Time complexity: O(n)
                Space complexity: O(n)

            3. APPROACH (Recussive DFS - Iterative):
            - Start from root - maintain [node, depth] for each node.
            - Add the node and depth to the stack.
            - Until the stack is not empty - untill you reach the end of the tree - keep checking child nodes.
                - Now retreive the node and the depth from the stack for the current level.
            - If the retreived node exisit then update res - if depth > res
            - Append the left and right child of curr_node to the stack.
            - Keep repeating utill all nodes go through this
            - Return the result (depth)
                Time complexity: O(n)
                Space complexity: O(n)  
        """
        #1. APPROACH (Recussive DFS) - Recussive DFS
        height = 0
        if not root:
            return 0
        height = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return height

        #2. APPROACH 2 (Recussive BFS - Level Order Traversal): Recussive BFS
        height = 0
        q = deque()
        q.append(root)
        if not root:
            return 0
        while q:
            for i in range(len(q)):
                curr_node = q.popleft()
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            height+=1
        return height

        # 3. APPROACH (Recussive DFS - Iterative):
        stack = [[root,1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res