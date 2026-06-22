class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Stack to retrive the latest occurance of the opening brackets in the given order.
        mystack = []
        # Have a mapping of which close brackers needs to have which open brackets:
        CloseToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            #if this character is a closing parenthesis, check by key present in hashmap:
            if c in CloseToOpen:
                #If this is a closing, then first check if there was anything in the stack at all, and if yes is the lastest opening bracket a the match for this:
                if mystack and mystack[-1] == CloseToOpen[c]:
                    mystack.pop()
                #If our stack is empty or is the latest opening in the stack is not a match:
                else:
                    return False
            #If not found in CloseToOpen then is a open parenthesis, keep adding them to the stack in order:
            else:
                mystack.append(c)
        #If my stack is still not empty that means we had a open that doesn't have a closing in s:
        return not mystack