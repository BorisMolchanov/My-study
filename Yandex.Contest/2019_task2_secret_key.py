import math

x, y = map(int, input().split())

lst = []  # в список будем складывать подходящие пары закрытого ключа sk(p,q)

for p in range(x, y + 1, x):  # оптимизируем перебор, добавляя шаг x = НОД
    for q in range(x, y + 1, x):
        if math.gcd(p, q) == x and math.lcm(p, q) == y:
            sk = (p, q)  # закрытый ключ найден
            lst.append(pk)
print(len(lst))  # длина списка = количество пар значений 
