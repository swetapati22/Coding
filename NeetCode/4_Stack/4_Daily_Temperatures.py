class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Time = O(n)
        Space = O(n)
        """
        #Keep adding to the stack, check if the current value is greater than any of its previously added temperatures.
        my_stack = []
        res = [0]*len(temperatures)
        #Store the val and the temperature index to the stack as a list.
        for idx, val in enumerate(temperatures):
            #Keep checking if the curent number is greater than the top value in the stack, keep repeating untill the condition satisfies (inorder of which they were added)
            while my_stack and my_stack[-1][0] < val:
                #If found then pop the top of the stack and calculate the gap between both to determine after how many days.
                stack_val, stack_idx = my_stack.pop()
                res[stack_idx] = idx - stack_idx
            my_stack.append([val, idx])
        return res

        