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

# x = 'hello'
# print('heyy'+x)

# x = 'hello'
# print(x[4])

# x = 'handwritten notes'
# print(x[4:-5])

# x = 'handwritten notes'
# print(x[-5:-1])

# x = 'handwritten notes'
# print(x[-5:])

# x = 'handwritten notes'
# print(x[:11])

# x = '      familiar with TanStack and React Query.     '
# print(x.strip())

# x='  77'
# print(x.isdigit())

# y = 'familiar with TanStack and React Query.'
# print(y.find('and'))

# print('0,0,1,0,1,0,1,0,1'.replace('0','1'))
# print('0,0,1,0,1,0,1,0,1'.replace('1','0'))

# print(type('full stack react framework - tanstack'.split('a',maxsplit=1)))

# print('full stack react framework - tanstack'.count('a'))

# print(int(True))

# x = 'hello'
# y = 'heyy'+"".join(x)
# print(y)

# x = ["apple", "banana", "orange"]
# print(", ".join(x))

# x1 = 'google.com'
# def counting(x):
#     dict = {}
#     for i in x:
#         key = dict.keys()
#         if i in key:
#             dict[i]+=1
#         else:
#             dict[i]=1
#     return dict
# print(counting(x1))

# ex = [1,2,3,4,5,6,7,8,9,10]
# ex[2:8]=[]
# print(ex)

# ex = 'w3resource'
# new = ex[:2]+ex[-2:]
# print(new)

# ex='w3'
# print(ex+ex)

# x='w'
# print(x.clear())

# ex = 'w3resource'
# def strings(x):
#     if len(x)<2:
#         return ""
#     return x[:2]+x[-2:]
# print(strings(ex))
# print(strings('ex'))
# print(strings('x'))

# x=int(input('enter a number : '))
# for i in range(0,x):
#     if i%2!=0:
#         print('weird')
#         break
#     elif i%2==0 and i in range(2,5):
#         print('not weird')
#         break
#     elif i%2==0 and i in range(6,20):
#         print('weird')
#         break
#     elif i%2==0 and i>20:
#         print('Not weird')
#         break
    
    
# x = 'restart'
# y=''
# for i in x:
#     print(x[i])
    
# def repeating(x):
#     first = x[0]
#     modified = first
#     for i in x[1:]:
#         if i == first:
#             modified += '$'
#         else:
#             modified +=i
#     return modified
# print(repeating('restart'))

# s,b = 'abc', 'xyz'
# def twist(x,y):
#     new = x[:2]+ y[-1:]
#     new2 = y[:2]+x[-1:]
#     add = new + ' ' + new2
#     return add
# print(twist(s,b))

# def correct(x):
#     if len(x)<=3:
#         return x + 'ing'
#     elif len(x)>3:
#         return x + 'ly'
#     else:
#         return x
    
# print(correct('adipwo'))

# def joining(str,x):
#     a = str[:x]
#     b = str[x+1:]
#     return a + b
# print(joining('programming',5))

# x = 'red, white, black, red, green, black'
# print(x.sorted())

# txt = "Hello My Name Is PETER"
# x = txt.swapcase()
# print(x)

# def multi(x):
#     if len(x)>4:
#         return x[::-1]
#     else:
#         return x
# print(multi('catss'))

# x = 'hello world \n'
# def remov(a):
#     return a.rstrip()
# print(remov(x))

# x = ["apple","ball","cat"]
# new = " ".join(x)
# print(new)

# x = "mishal ummer"
# new = ""
# for i in x:
#     if i not in new:
#         new += i
# print(new)

