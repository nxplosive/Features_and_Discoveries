# Изменяемые списки

from copy import deepcopy

l1 = [1, 2, 3, [4], [5, 6, 7]]
# l2 = l1.copy()
l2 = deepcopy(l1)
l2.append([9])
l2[-2].append(8)

print(l1)
print(l2)

# Кортежи

t1 = (1, 2, 3, 4, 5) # неизменяемый
t2 = t1 # копируется не меняя оригинал автоматически

print(t2)

frozenset({1, 2, 3, 4, 5, 5, 5, 5}) # неизменяемое множество