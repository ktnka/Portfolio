'''
Треугольник Паскаля 1 🌶️

Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов,
имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы.
Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число n. Напишите программу, которая возвращает указанную
строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).
'''

def pascals(row, rows):
    lst = [0] * rows
    for i in range(rows):
        for j in range(i + 1):
            lst[i] = [1] * (j + 1)

    for i in range(2, rows):
        for j in range(1, i):
            lst[i][j] = lst[i - 1][j - 1] + lst[i - 1][j]
    print(lst[row])

pascals(30, 40)