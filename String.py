# ####   Input: num1 = "456", num2 = "77"
# ####   Output: "533" 
# num1 = "456"
# num2 = "77"
# ####   Output: "533"
# x = int(num1)+int(num2)
# print(x)

# # All letters in this word are capitals, like "USA".
# # All letters in this word are not capitals, like "leetcode".
# # Only the first letter in this word is capital, like "Google".

# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         if word.isupper():
#             return True
#         if word.islower():
#             return True
#         if word[0].isupper() and word[1:].islower():
#             return True
#         return False

# s = "hello world"
# r = ""
# for i in s:
#     r = i+r
# print(r)

#Write a Python program that check if a string only contains numbers. If it does, print True. Else, print False.

# def string(x):
#     try:
#         return x.isnumeric()
#     except AttributeError:
#         return False
# y = input("enter a string :")
# result = string(y)
# print(result)

