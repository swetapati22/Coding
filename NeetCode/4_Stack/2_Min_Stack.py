class MinStack:
    """
    Time: O(1)
    Space: O(2n) = O(n)
    """

    #Create two list - one acts as stack and another as min stack
    def __init__(self):
        self.stack = []
        self.minstack = []
        min_val = ("-inf")
        
    #Stack push is straight forward, pushing to min_stack needs to check current min value vs the curr value in consideration
    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = (val if not self.minstack else min(val, self.minstack[-1]))
        self.minstack.append(min_val)    

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