# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

my_list = [-2, 4, -5, 7, 3, 1]

total = 0
for i in my_list:
    total = i + total
    i += 1
print(f"{total}")
