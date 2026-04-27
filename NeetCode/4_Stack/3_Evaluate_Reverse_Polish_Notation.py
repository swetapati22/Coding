class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Approach:
        Time: O(2n) -> O(n) -> Parsing through the stack once to add and then remove from the stack once.
        Space: O(n) -> Using a stack
        """
        my_stack = []
        #This can be solved through a bunch of if else conditions, do the operations by poping the two integers we push to the stack before an operator appears. 
        #Main task is for division, where we have to floor the output (truncates toward zero), so we can use a int to do the same.
        for c in tokens:
            if c == "+":
                my_stack.append(my_stack.pop() + my_stack.pop())
            elif c == "-":
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(b-a)
            elif c == "*":
                my_stack.append(my_stack.pop() * my_stack.pop())
            elif c == "/":
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(int(b/a))
            else:
                my_stack.append(int(c))
        return my_stack.pop()