"""
D. Разгадай шифр

Язык	        Ограничение времени	  Ограничение памяти
Все языки	    1.4 секунды	          33Mb	
Oracle Java 7	9 секунд	          286Mb
Python 3.7.3	1.5 секунд	          38Mb
Oracle Java 8	9 секунд	          286Mb
Node JS 8.16	15 секунд	          256Mb

Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Шерлок Холмс и доктор Ватсон передают друг другу зашифрованные сообщения, состоящие из чисел. 
Каждое число может обозначать одну букву, слово или знак препинания. 
Получая последовательность чисел, Холмс и Ватсон могут расшифровывать сообщения друг друга. 
Однако они стали подозревать, что кто-то разгадал их шифр и повысили уровень безопасности. 
Теперь каждое сообщение зашифровано в матрице. 
Чтобы его прочитать, нужно распечатать значения матрицы по спирали, начиная от центра вверх и далее по часовой стрелке.

Формат ввода
Первая строка содержит целое нечётное число m в диапазоне от 1 до 1000 — количество строк и столбцов матрицы.
В каждой из следующих m строк даны m целых чисел в диапазоне от -1000 до 1000, разделённых пробелом.

Формат вывода
Нужно вывести значения в матрице, начиная с центра по спирали. 
Движение вверх, далее по часовой стрелке. Каждое число выводится в отдельной строке.

Пример 
Ввод	    Вывод 7 10 7 7 4 3 8 0 9
3
9 10 7
0 7 7
8 3 4
"""

m = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(m)]
x, y = m // 2, m // 2 # center (x: № of row, y: № of col)
up, right, down, left = 1, 1, 2, 2

for _ in range(m // 2): # count of complete spirals
    # moving up
    for x_ in range(x, x - up, -1):
        print(matrix[x_][y])
    x = x_ - 1 # change x

    # moving right
    for y_ in range(y, y + right):
        print(matrix[x][y_])
    y = y_ + 1 # change y

    # moving down
    for x_ in range(x, x + down):
        print(matrix[x_][y])
    x = x_ + 1 # change x

    # moving left
    for y_ in range(y, y - left, -1):
        print(matrix[x][y_])
    y = y_ - 1 # change y

    # change up, right, down, left
    up += 2
    right += 2
    down += 2
    left += 2

# print left column (bottom-up)
for x_ in range(x, -1, -1):
    print(matrix[x_][y])