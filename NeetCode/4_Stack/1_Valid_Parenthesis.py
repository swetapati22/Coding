class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach: Using stack for chekcing if the last found open parenthesis was the open parenthesis to the closing parenthesis I have right now.
        Time: O(n)
        Space: O(n)
        """

        #We store the values in a stack:
        stack = []

        #Create a close to open mapper, since we need to ensure every closing bracket that we encounter had an immediate opening bracket in order:
        close_to_open = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        #Traverse the string:
        for p in s:
            #Check if what we encounter is an closing bracker, if yes then check the top of the stack to determine if the immediate previous bracket encounter is a opening bracket, if yes then pop the top value, if no - that means the top opening bracket didn't match the closing one then pop the same.
            if p in close_to_open:
                if stack and stack[-1] == close_to_open[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        #If we reach to the end of the string and my stack is not empty that mean there is some unordered brackets that don't have a matching closing - so return false, if stack is empty - that means we found all correct pairs, return true
        return True if not stack else False

        