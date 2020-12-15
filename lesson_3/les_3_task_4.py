# 4. Определить, какое число в массиве встречается чаще всего.

import random

a = [random.randint(0, 10) for _ in range(15)]
print(a)
b = list(set(a))
max_freq = 1
for i in range(len(b)):
    freq = 1
    for j in range(len(a)):
        if a[j] == b[i]:
            freq += 1
    if freq > max_freq:
        max_freq = freq - 1
        num = b[i]

if max_freq > 1:
    print(f'Число {num} встречается {max_freq} раз')
else:
    print('Все числа уникальны')