# my_dict = {
#     'Macbook': 'pro',     #key: value
#     'Tesla': 'X'
# }
# key = 'Honda'
# value = 'Cv'
# my_dict[key] = value  #додає нові ключі зі змінними в словник
# print(my_dict)
# print(my_dict['Macbook']) #принтує значенння ключа
# thisdict = dict(name = 'Sarah', age = 14, country = 'Spain')
# thisdict['age'] = True
# print(thisdict.keys())   #виводить ключі слованику, values = виводить всі значення словнику
# print(thisdict.items())  #виводить весь словник
# thisdict.pop('age')      #видаляє за ключем
# thisdict.popitem()       #видаляє останій елемент
# del thisdict['age']      #видаляє елементи в словнику, або весь словнику
# for x in thisdict:
#     print(thisdict[x])
# for x in thisdict.values():
#     print(x)
# for x,y in thisdict.items():  #в х записуються ключі, а в у записуються значення
#     print(x,y)
# thisdict = dict(name = 'Sarah', age = 14, country = 'Spain')
# my_dict = thisdict.copy()     #копіює словник
# print(my_dict)
# my_dict['new_key'] = 'new_value'
# print(thisdict)
# print(my_dict)
# my_dict = {
#     'Nick':{
#         'phone': "11111",
#         'insta': '@123'
#     },
#     'Anna':{
#         'phone': "2222",
#         'insta': '@344'
#     },
#     'Rick': {
#         'phone': "333",
#         'insta': '@544'
#     }
#     }
# a = input()
# if a == my_dict.keys():
#     print(my_dict.values())
# user = my_dict['Anna']['phone']  # ---> 2222
# my_dict['Anna']
# print(user)
# a = input()
# my_dict = {
#     a: 'black'
# }
# print(my_dict)
my_dict = {
    'One': '1',
    'two': '2',
    'three': '3'
}
# del my_dict['two'], my_dict['three']
# print(my_dict)

deleted = ['two', 'three']
for x in deleted:
    my_dict.pop(x)

print(my_dict)
