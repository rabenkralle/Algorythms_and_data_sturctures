# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-100, 100) for _ in range(10)]
print(a)
index = -1

for i in range(len(a)):
    if a[i] < 0 and index == -1:
        index = i
    elif a[i] < 0 and a[i] > a[index]:
        index = i

print(f'Максимальное отрицательное значение {a[index]} на позиции {index+1}')