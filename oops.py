# class demo():
#     def __init__(self):
#         print("constructor")
    
#     def hello(self):
#         print("method")
        
# obj1 = demo()
# obj2 = demo()
# obj3 = demo()
# obj2.hello()
        
# class greeting():
#     # @staticmethod
    
#     def hello(self,x):
#         print("good morning" ,x)
        
# obj1 = greeting().hello("vicky")
# obj2 = greeting().hello("mishal")

# class demo:
#     x = 10
    
# obj = demo()
# obj.x = 40
# print(obj.x)

# class demo:
#     def __init__(self,x,y,z):
#         print(x,y,z)
#     def __init__(self,x,y):
#         print(x,y)
        
# obj = demo(10,11)

# class demo():
#     def __init__(kuttimon,x,y):
#         kuttimon.x = x
#         kuttimon.y = y
#     def display(kuttimon):
#         print(kuttimon.x,kuttimon.y)
        
# obj = demo(10,20)
# obj.display()

# class demo():
#     def __init__(self):
#         pass
    
# obj = demo()
# obj.x = 10
# obj.y = 220
# print(obj.x)

# class demo():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def show1():
#         pass
#     def show(self):
#         print(self.x)
#         print(self.y)
    
# obj = demo(111,2222)
# obj.show()
    
# class demo():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def show1():
#         pass
#     def show(self):
#         print(self.x)
#         print(self.y)
    
# obj = demo(111,2222)
# obj.show()
        
# class demo():
#     def __init__(self):
#         self.x = "mishal"
#         self.y = 25
#         self.z = "batch-20"
        
# obj = demo()
# # print(obj.x)
# # print(obj.z)
# # print(obj.y)
# print(obj.__dict__)
        
# class demo:
#     def __init__(self):
#         self.x = 10
#         self.y = 20
#         self.z = 30
#         del self.y
        
# print(demo().__dict__)
        
# class demo:
#     def __init__(self):
#         self.x = 10
#         self.y = 20
#         self.z = 30
#         self.a = 50

# obj = demo()
# del obj.a        
# print(demo().__dict__) 
# print(obj.__dict__)        

# class demo:
#     x=20
#     def init(self):
#         self.x = 10
# obj = demo()
# print(obj.x)
# obj.init()
# print(obj.x)

# class demo:
#     x=20
#     a=9
#     def init(self,m):
#         self.x = m
#         print(self.a)

# obj = demo()
# obj2 = demo()
# print(obj.x)
# obj.init(30)
# obj2.init(50)
# print(obj.x)
# print(obj2.x)
# obj.x=20000
# print(obj.x)
        
# class demo:
#     x = 1111
#     def show(self):
#         y = 2222
        
# obj = demo()
# obj.x = 10            ??????????????????????????????????????????????????????????????????????
# print(obj.x)

# obj.show()
# obj.y = 20
# print(obj.y)

        
# class demo:
#     x = 1111
    
#     def show(self):
#         y = 2222
        
# obj = demo()
# obj.x = 10
# obj2 = demo()
# print(obj.x)

# obj.show()
# obj.y = 20
# print(obj.y)
# print(obj2.y)

# class demo:
#     x = 1111
    
#     def show(self):
#         y = 2222
        
# obj = demo()
# obj.x = 10
# obj2 = demo()
# print(obj.x)
# print("obj2",obj2.x)
# obj.show()
# obj.y = 20
# print(obj.y)
# # print(obj2.y)

# class demo:
#     x = 1111
    
#     def show(self):
#         self.y = 2222
#         return self.y
        
# obj = demo()
# obj.x = 10
# obj2 = demo()
# print(obj.x)
# print("obj2",obj2.x)
# inner_y = obj.show()
# obj.y = 20
# print(inner_y)
# print(obj.y)
# # print(obj2.y)
        



























