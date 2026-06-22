class MinStack:
    """
    Time Complexity: O(1)
    Space Complexity: O(2n) = O(n)
    """

    #Create two list - one acts as stack and another as min stack
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    #Stack push is straight forward, pushing to min_stack needs to check current min value vs the curr value in consideration
    def push(self, value: int) -> None:
        self.stack.append(value)
        # in order to check if curr val is less than the previous minstack value, ensure minstack was present
        val = min(value, self.minstack[-1] if self.minstack else value)
        self.minstack.append(val)  

    #Pop top value from both stack and minstack
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    #Display the value at the top of the stack
    def top(self) -> int:
        return self.stack[-1]
        
    #Display the value at the top of the minstack
    def getMin(self) -> int:
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()