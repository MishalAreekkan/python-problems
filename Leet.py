# # is palindrome
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         string = str(x)
#         if string == string[::-1] :
#             return True
        
# # game divisor
# class Solution:
#     def divisorGame(self, n: int) -> bool:
#         if n%2!=0:
#             return False
#         else:
#             return True
# # maximum wealth finder
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         max_total = 0
#         for i in accounts:
#             total = sum(i)
#             if total>max_total:
#                 max_total = total
#         return max_total

# # fliping
# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         for i in image:
#             i.reverse()
#             for j in range(len(i)):
#                 i[j]=1-i[j]
#         return image
    
    
# # sqaure root
# class Solution:
#     def mySqrt(self, x: int) -> int:
        
#         return int(math.sqrt(x))


 
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         x = [i**2 for i in nums]
#         x.sort()
#         return x 


# 26################
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # new= []
#         # for i in nums:
#         #     if i not in new:
#         #         new.append(i)
#         #     new.sort()
#         # return len(new)

#         s = set(nums)
#         nums.clear()
#         print(nums)
        
#         for i in s:
#             nums.append(i)
#         nums.sort()
#         return len(nums) 