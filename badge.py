# def squaring(x):
#     for i in x:
#         yield i **2

# x = squaring(l)
# print(x)

# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)
 
# result = outer_function(5, 10)
# print(result)
# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))

# x = [i for i in range(0,1001) if i % 7 == 0]
# print(x)
# def facto(n):
#     if n ==0:
#         return 1
#     else:
#         x = 1
#         i = 1
#         while i<=n:
#             x *= i
#             i += 1
#         return x
    
# print(facto(5))

# def facto(n):
#     if n == 0:
#         return 1
#     else:
#         return n * facto(n-1)
    
# print(facto(5))

# l = lambda x:x*4
# print(l(5))

# def greeting(x):
#     y = lambda greet:f"{greet} {x}"
#     return y("hello")
    
# print(greeting("mishal"))

# l = [1,2,3,4,5]
# x  = lambda x:x*2
# result = map(x,l)
# print(set(result))

# l = range(1,20)
# x = lambda x : x%2 ==0
# result = filter(x,l)
# print(list(result))

# from functools import reduce
# x = [1,2,3,4,5]
# l = lambda x,y : x + y
# result = reduce(l,x)
# print(result)

# class loop:
#     def __init__(self,initial,final):
#         self.initial = initial
#         self.final = final
        
#     def __iter__(self):
#         return self
        
#     def __next__(self):
#         if self.initial > self.final:
#             return StopIteration
#         else:
#             self.initial += 1
#             return self.initial - 1
                
# l = loop(1,5)
# print(next(l))
# print(next(l))

# def gener(start,end):
#     current = start
#     while current<end:
#         yield current
#         current += 1
        
# new = gener(1,5)
# print(next(new))
# print(next(new))
# print(next(new))