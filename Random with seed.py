import random

#ranodm changing
print(random.randint(0,100))
print(random.randint(0,100))

#static
random.seed("abc")
print(random.randint(0,100))
print(random.randint(0,100))