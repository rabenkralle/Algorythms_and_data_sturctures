# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите число: ')
even = 0
odd = 0
even_list = []
odd_list = []
for i in number:
    if int(i) % 2 == 0:
       even += 1
       even_list.append(i)
    else:
        odd += 1
        odd_list.append(i)
print(f'Четных чисел: {even} шутк, {even_list}')
print(f'Нечетных чисеk: {odd} штук, {odd_list}')