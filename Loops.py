# required_number = 7
# user_number = random.randint(0, 10)
#
# while required_number != user_number:
#     user_number = random.randint(0, 10)
#     print(f'Пользователь ввёл число {user_number}')
#
# iterations_count = 10
# i = 0
# while i < iterations_count:
#     print(f"Текущая итерация: {i}")
#     i += 1

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]
from pprint import pprint

for user in users:
    pprint(f"Пользователю {user['name']} {user['age']} лет")

d = {
    "first": 1,
    "second": 2,
    "third": 3
}
for item in d:
    pprint(item)
print()
for item in d.keys():
    pprint(item)
print()
for item in d.values():
    pprint(item)
print()
for item in d.items():
    pprint(item)
print()
for (key, value) in d.items():
    print(f"Ключ: {key}, Значение: {value}")

print(list(range(10)))

iterations_count = 10
for i in range(5, iterations_count, 2):
    print(f"Current iteration is: {i}")

for i in range(iterations_count):
    if i % 2 == 0:
        continue
    if i > 7:
        break
        print("Ill never done")
    print(f"Точное нечётное число: {i}")

for i in range(5):
    for j in range(3):
        print(i, j)

cities = ["Ekaterinburg", "Moscow", "Sochi"]
for i, city in enumerate(cities):
    print(f"{city} at {i + 1} place of air pollution")