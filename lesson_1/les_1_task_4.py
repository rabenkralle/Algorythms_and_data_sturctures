# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

l1 = ord(input('Введите первую букву: '))
l2 = ord(input('Введите вторую букву: '))

print(f'Позиция первой буквы: {l1 - 96}')
print(f'Позиция второй буквы: {l2 - 96}')

print(f'Между буквами {abs(l2 - l1)} букв')