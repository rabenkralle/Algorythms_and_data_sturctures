# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

pos = int(input('Введите позицию буквы: '))

print(f'Это буква: {chr(96 + pos)}')