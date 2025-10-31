#Question: https://leetcode.com/problems/min-stack/description/

##################### QUESTION #####################
# 155. Min Stack - Medium
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 
# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

##################### SOLUTION #####################
class MinStack:
    """ 
    COMPANYs - AMAZON
    APPROACH (Brute Force):
    - Traverse the stack each time on querying min value at any time to find the min value.
        Time complexity: O(n)
        Space complexity: O(1)

    APPROACH (Optimal):
    - Create another stack called min stack and store the minimum at current state all the time, each index will contain the min value until its incersion, so that you can always pop the top and the 
        Time complexity: O(1)
        Space complexity: O(n)
    """

    def __init__(self):
        self.min_list = []
        self.val_list = []

    def push(self, val: int) -> None:
        self.val_list.append(val)
        if not self.min_list:
            self.min_list.append(val)
        else:
            self.min_list.append(min(self.min_list[-1],val))

    def pop(self) -> None:
        self.val_list.pop()
        self.min_list.pop()

    def top(self) -> int:
        return self.val_list[-1]

    def getMin(self) -> int:
        return self.min_list[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()