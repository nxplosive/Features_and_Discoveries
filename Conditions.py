b = bool
t = True
f = False
n = None
if t:
    print("Я выполняюсь")
if f:
    print("Я никогда не выполнюсь")
code = 300
if 200 <= code < 400:
    print("Проверка пройдена, хороший ответ!")
elif 400 <= code < 600:
    print("Плохой код ответа")
else:
    print("Какой-то старнный код")

user_list = []
if user_list == []:
    pass
if user_list:
    print("List not empty")
items_count = 0
if items_count == 0:
    pass
if items_count:
    print("Count != 0")

print(bool(100))
print(bool(-100))
print(bool(0)) #False
print(bool('abc'))
print(bool("")) #False
print(bool([])) #False
print(bool([1, 2, 3]))
print(bool([False]))