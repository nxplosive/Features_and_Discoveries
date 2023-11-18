# # Elements
# l = [1, 2, 3, "a", "b", "c", [4, 5, 6]]
#
# print(l[4])
# print(l[-1])
# print(l[-1][1]) #element inside of list
# print(l[::-1])
#
# #l.append("new element") #добавить элемент в конец списка
# #l.extend(["elem", "another elem"])
# #l.reverse()
# print(len(l)) #длина строки
# print(l)
# l[1] = 200 #заменить элемент
# print(l)


# Multiples

s1 = {1, 2, 3, 4, 5, 5, 5, 5}
s2 = {1, 2, 5, 5, 5}
print(s1)
print(s2)

x = s1.intersection(s2)
y = s1 - s2
print(x, y, sep='\n')

print([1, 2, 3, 4, 5, 5, 5, 5]) #список
print(set([1, 2, 3, 4, 5, 5, 5, 5])) #привести список в множество
print(list(set([1, 2, 3, 4, 5, 5, 5, 5]))) #привести множество обратно в список


# # Словари
#
# d = {
#     "key": "value",
#     "another": "another value"
# }
#
# user1 = {
#     "name": "Vasya",
#     "age": 18
# }
#
# user2 = {
#     "name": "Petya",
#     "age": 20
# }
#
# users = {
#     123: user1,
#     456: user2
# }
#
# users[555] = {
#     "name": "Oleg",
#     "age": 25
# }
#
# #print(user1["name"])
# #print(user2["name"])
# print(users.get(123))
# print(users[456])
# print()
# print(users.get(50, {"name": "default user"})) #если такого пользователя нет, то выводится значение по умолчанию, которое занесено в фигурные скобки
# print(users.get(123, {"name": "default user"}))
# print(users.get(555))
# print("----------")
#
# from pprint import pprint
#
# pprint(list(users.items()))
