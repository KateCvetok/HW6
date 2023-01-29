# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random
n = int(input("Сколько элементов? "))
list1 = []
for i in range(n):
    list1.append(random.randint(1, 10))
print('Cделан такой список -', list1)


number_of_elements = len(list1)
number_of_unique_elements = len(set(list1))

print("Количество различных элементов в списке: ", number_of_unique_elements)
