"""
F. Три фишки

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Гарри Поттер и Гермиона играют в игру. У Гермионы есть фишки с указанным на них количеством очков. 
На каждой фишке — k очков, k находится в промежутке от −10**5 до 10**5. 
Гарри называет число, а Гермиона должна выбрать три фишки, сумма очков на которых наиболее близка с заданному числу. 
Долго же будет маленькая волшебница искать нужные фишки! Помогите ей справиться с задачей скорее.

Формат ввода
Первая строка содержит целое число n в диапазоне от -10**5 до 10**5, число, названное первым участником. 
Во второй строке через пробел заданы целые числа в диапазоне от -10**5 до 10**5, — очки для фишек второго участника. 
Их количество может быть от 3 до 10**4.

Формат вывода
Нужно вывести целое число — сумму очков трёх фишек, наиболее близкую к n.

Пример 1
Ввод	         Вывод 1
6
-1 -1 -9 -7 3 -6

Пример 2
Ввод	         Вывод 6
5
7 -8 2 -8 -3

Пример 3
Ввод	         Вывод 8
8
6 2 8 -3 1 1 6 10

Примечания
Решение должно работать не дольше, чем за O(n**2). Ограничение по памяти — O(1). 
Гарантируется, что для всех тестовых примеров в задаче может быть только 1 верный ответ.

!!!Не проходит лимит по времени!!!
"""

from itertools import combinations

n = int(input())
seq = [int(i) for i in input().split()]
min_dist = 4 * 10**5

for triple in combinations(seq, 3):
    dist = abs(n - sum(triple))
    if dist < min_dist:
        sum_ = sum(triple)
        min_dist = dist

print(sum_)