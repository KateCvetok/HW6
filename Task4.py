# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.

N = int(input('Количество друзей: '))
dict_list = []
for i in range(N):
    name = input('Имя друга: ')
    age = int(input('Возраст друга: '))
    dict_list.append({'name': name, 'age': age})
# print(dict_list)
sum = 0
max_name = dict_list[0]['name']
for i in dict_list:
    sum += i['age']
    if len(i['name']) > len(max_name):
        max_name = i['name']
print(sum / N)
print(max_name)
