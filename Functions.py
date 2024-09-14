# Type of Function	
# No Parameters, No Arguments	
# Parameters, No Default Values	
# Parameters with Default Values	
# Variable Positional Arguments	
# Variable Keyword Arguments	
# Both Positional and Keyword Arguments	
# Keyword-Only Arguments


# def first():
#     def second():
#         print('1st')
#     second()
#     print('2nd')
        
# first()

# def first(x):
#     def second():
#         return 'hello'
#     result = second() + x + 'all'
#     return result
# print(first(" "))

# passsinf a function as argument
# def first(x):
#     return '1sttt' + " " + x()
    
# def second():
#     return '2nd oneee'
    
# print(first(second))

# Function returning another Function in Python

# def first():
#     def second():
#         return '1sttt' + " "
#     return second()
    
# print(first())

# x = [1,2,3,4,5,6]
# l = lambda x:x**2
# m = list(map(l,x))
# print(m)

# x = lambda a,b:a*b
# print(x(10,50))

# x = lambda a,b:(a*b,a**b)
# i,j = x(10,50)
# print(j)

# lam = lambda x=10 : (lambda y : x+y)
# a = lam()
# print(a(15))

# lam = (lambda x:x*2)(5)
# print(lam)