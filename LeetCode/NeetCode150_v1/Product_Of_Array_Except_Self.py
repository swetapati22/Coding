# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#     """ 
#     APPROACH: BRUTE FORCE:
#         - For each index, iterate through the entire array
#         - Multiply all elements except the current one
#         - Store that product in the result array

#         Time Complexity: O(n^2)
#         Space Complexity: O(1) auxiliary space
#     """

#     ######## BRUTE FORCE ########
#         result = []

#         for i in range(len(nums)):
#             prod = 1
#             for j in range(len(nums)):
#                 if i != j:
#                     prod *= nums[j]
#             result.append(prod)

#         return result

#     """
#     APPROACH (Optimal):
#         - Initialize a prefix and postfix with 1
#         - The trick here is to go through the list and while going through the list the result should be first operated with the prefix (initially 1), and then update the prefix, so that when we traverse the list for each current element we use the prefix updated till curr_position - 1, i.e till the previous value.
#         - Similarly for the postfix (traverse the array from back to front)
#         - While traversing back, remember to update the result not overide as the result has the prefix values.
#         - If after complete traversal (once for updating prefix and another for postfix) - return result.
#             Time complexity: O(n)
#             Space complexity: O(1)
#     """
#     ######## Optimal ########
#         result = [1]*len(nums)
#         prefix = 1
#         for i in range(len(nums)):
#             result[i] = prefix
#             prefix *=nums[i]
#         postfix = 1
#         for i in range(len(nums)-1,-1,-1):
#             result[i]*=postfix
#             postfix *= nums[i]
#         return result

