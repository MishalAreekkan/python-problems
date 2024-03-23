# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# Exercise 5 - make a list that contains each fruit with more than 5 characters

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.

""""""""""""
## ANSWERS ##


# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# updated = [x.upper() for x in fruits]
# print(updated)

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# updated = [x.capitalize() for x in fruits] 
# print(updated)

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange','anss']
# vowels = ['a','e','i','o','u']
# updated = [sum(x in vowels for x in frui) for frui in fruits]
# print(updated)

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange','anss']
# updated = [x for x in fruits if len(x)>5]
# # print(updated)

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange','anss']
# updated = [x for x in fruits if len(x)==5]
# print(updated)

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange','anss']
# updated = [len(p) for p in fruits]
# print(updated)

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange','anss']
# updated = [(x for x in i if x == "a")for i in fruits]
# print(updated)

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# even = [x for x in numbers if x%2==0]
# print(even)


# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# positive = [x for x in numbers if x >0]
# print(positive)
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# two_numeric = [x for x in numbers if x>10]
# print(two_numeric)

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# two = [[int(digit) for digit in str(num) if len(str(num)) > 2] for num in numbers]
# print(two)

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# sqr = [x**2 for x in numbers]
# print(sqr)

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# odd_neg = [x for x in numbers if x<1 or x%2!=0]
# print(odd_neg)
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# updated = [x+5 for x in numbers]
# print(updated)
# {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}
# l="GFG"
# new_dict = {x:{y:x+y for y in l} for x in l}
# # print(new_dict)
# simple_dict = {x:{y:y+x for y in l} for x in l}
# print(simple_dict)


# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# new_dict = {x:words.count(x) for x in set(words)}
# print(new_dict)

# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# updated = [x for y in matrix for x in y]
# print(updated)

# l1 = [1,2,3,4,5]
# l2 = [4,5,6,7,8,9]
# l1.extend(l2)
# result = []
# for i in l1:
#     if i not in result:
#         result.append(i)
# print(result)

