# ###  upadting###
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict["emp3"]["salary"] = 8500
# print(sample_dict)
# #############################################################
# # random offers for customers
# import random
# customer = ["appu","doppu","shukur","ssuuii","kumar"]
# offers = {x:random.randint(1,100) for x in customer}
# print(offers)

# # days and temp
# days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

# weather = {x:y for x,y in zip(days,temp_C)}
# print(weather)
# #
# words = ['data', 'science', 'machine', 'learning']
# d = {x:len(x) for x in words}
# print(d)

# d ={"name":"mishal","place":"malaprm","state":"kerala"}
# l = [1,2,3]
# dic = {x:y for x,y in zip(d.values(),l)}
# print(dic)

# d ={"name":"mishal","place":"malaprm","state":"kerala"}
# dic = {x:y for x,y in zip(d.values(),d.keys())}
# print(dic)

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# d = {(x,y):x*y  for x in a for y in b}
# print(d)

# #######  fromkeys()  ###########

# d = dict.fromkeys(range(6),[])
# d[0].append(2)
# print(d)

# users = [
#     (0, "Bob", "password"),
#     (1, "code", "python"),
#     (2, "Stack", "overflow"),
#     (3, "username", "1234"),
# ]
# Y = {user[0]: user for user in users}
# print(Y)

# import random
# list1 = ["mis","sui","yaz","ans","vicky","niz"]
# score = {x:random.randint(50,100) for x in list1}
# print(score)

# new_score = {'mis': 58, 'sui': 94, 'yaz': 71, 'ans': 53, 'vicky': 81, 'niz': 96}

# dic = {x:y for (x,y) in new_score.items() if y>80}

# print(dic)

# import pandas 

# student_score = {
#     "student" : ["mishal","yaz","ssuiii","ansas","vicky"],
#     "score":[55,65,75,85,95]
# }
# # for (x,y) in student_score.items():
# #     print(y)

# newone = pandas.DataFrame(student_score)
# print(newone)