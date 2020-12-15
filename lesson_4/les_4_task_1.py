# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


import cProfile

def div_count_1(number):
    l = [0] * 8

    for i in range(2, number):
        for j in range(2, 10):
            if i % j == 0:
                l[j - 2] += 1

    return l

# py -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.div_count_1(99)"
# 100 loops, best of 5: 65.9 usec per loop
# "les_4_task_1.div_count_1(200)"
# 100 loops, best of 5: 134 usec per loop
# "les_4_task_1.div_count_1(500)"
# 100 loops, best of 5: 338 usec per loop
# "les_4_task_1.div_count_1(1000)"
# 100 loops, best of 5: 689 usec per loop
# "les_4_task_1.div_count_1(10000)"
# 100 loops, best of 5: 7.14 msec per loop

# cProfile.run('div_count_1(10000)')
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.007    0.007    0.007    0.007 les_4_task_1.py:15(div_count_1)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def div_count_2(number):
    l = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(2, number):

        if num % 2 == 0:
            l[2] += 1

        if num % 3 == 0:
            l[3] += 1

        if num % 4 == 0:
            l[4] += 1

        if num % 5 == 0:
            l[5] += 1

        if num % 6 == 0:
            l[6] += 1

        if num % 7 == 0:
            l[7] += 1

        if num % 8 == 0:
            l[8] += 1

        if num % 9 == 0:
            l[9] += 1

    return l


# py -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.div_count_2(99)"
# 100 loops, best of 5: 40.1 usec per loop
# "les_4_task_1.div_count_2(200)"
# 100 loops, best of 5: 101 usec per loop
# "les_4_task_1.div_count_2(500)"
# 100 loops, best of 5: 208 usec per loop
# "les_4_task_1.div_count_2(1000)"
# 100 loops, best of 5: 420 usec per loop
# "les_4_task_1.div_count_2(10000)"
# 100 loops, best of 5: 4.45 msec per loop

# cProfile.run('div_count_2(10000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.004    0.004    0.004    0.004 les_4_task_1.py:44(div_count_2)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def div_count_3(number):
    l = dict()

    for div in range(2, 10):
        l[div] = number // div

    return l

# py -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.div_count_3(99)"
# 100 loops, best of 5: 882 nsec per loop
# "les_4_task_1.div_count_3(200)"
# 100 loops, best of 5: 878 nsec per loop
# "les_4_task_1.div_count_3(500)"
# 100 loops, best of 5: 881 nsec per loop
# "les_4_task_1.div_count_3(1000)"
# 100 loops, best of 5: 905 nsec per loop
# "les_4_task_1.div_count_3(10000)"
# 100 loops, best of 5: 957 nsec per loop

# cProfile.run('div_count_3(10000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:94(div_count_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ВЫВОД:
# Самый лучший алгоритм это div_count_3(). Он выполняется за самое короткое время. И слабо зависит от количества
# входных данных
