from operator import itemgetter
from pprint import pprint


def sum_numbers(a: int, b: int):
    print(a + b)


# raise AssertionError

sum_numbers(20, 15)
sum_numbers(10, 30)
sum_numbers(-735862386, 1)

sum_numbers("abc", "def")


def sum(a: int, b: int):
    return a + b


n = sum(10, 15)
print(n)

sum_numbers(a=4, b=6)


def multiply(n, mult: int = 2):
    print(n * mult)


multiply(10)
multiply(10, mult=5)

print(1, 2, 3, 4, 5, sep=" | ")


def return_tuple():
    return 1, 2, 3


t = return_tuple()
print(t)
t1, t2, t3 = return_tuple()
print(t1, t2, t3)

t1, *t2 = return_tuple()
print(t1, t2, t3)

t1, *_ = return_tuple()
print(t1)


def custom_print(*args):
    for arg in args:
        print(args)
        print(*args)


custom_print(1, 2, 3, 4, 5)


def custom_named_print(*args, **kwargs):
    print(args, kwargs)
    print(*args, **kwargs)


custom_named_print(1, 2, 3, 4, 5, end="!\n", sep="|")

p = print()

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]


def get_age(user):
    # pprint(user)
    return user["age"]


users.sort(key=get_age)
# users.sort(key=get_age, reverse=True)
pprint(users)
print()
users.sort(key=lambda user: user["age"])
pprint(users)
print()
users.sort(key=itemgetter("age"))
pprint(users)