# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(0, 1000) for _ in range(10)]
print(a)
min_a = 0
max_a = 0

for i in range(len(a)):
    if a[i] < a[min_a]:
        min_a = i
        
    elif a[i] > a[max_a]:
        max_a = i


a[min_a], a[max_a] = a[max_a], a[min_a]

print(a)