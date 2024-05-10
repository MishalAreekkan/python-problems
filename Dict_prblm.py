###  upadting###
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict["emp3"]["salary"] = 8500
print(sample_dict)
#############################################################
# random offers for customers
import random
customer = ["appu","doppu","shukur","ssuuii","kumar"]
offers = {x:random.randint(1,100) for x in customer}
print(offers)

# days and temp
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

weather = {x:y for x,y in zip(days,temp_C)}
print(weather)
#
words = ['data', 'science', 'machine', 'learning']
d = {x:len(x) for x in words}
print(d)

d ={"name":"mishal","place":"malaprm","state":"kerala"}
l = [1,2,3]
dic = {x:y for x,y in zip(d.values(),l)}
print(dic)

d ={"name":"mishal","place":"malaprm","state":"kerala"}
dic = {x:y for x,y in zip(d.values(),d.keys())}
print(dic)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
d = {(x,y):x*y  for x in a for y in b}
print(d)

#######  fromkeys()  ###########

d = dict.fromkeys(range(6),[])
d[0].append(2)
print(d)

users = [
    (0, "Bob", "password"),
    (1, "code", "python"),
    (2, "Stack", "overflow"),
    (3, "username", "1234"),
]
Y = {user[0]: user for user in users}
# print(Y)
