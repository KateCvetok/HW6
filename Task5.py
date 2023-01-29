# "Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка.
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке. Составьте словарь,
# в котором ключ - это английское слово, а значение - это список русских слов.
# В этой задаче нужно использовать строчный метод split().

K = int(input('Сколько слов нужно перевести: '))
translate_dict = {}
for i in range(K):
    eng_rus_str = input()
    some_list = eng_rus_str.split(' - ')
    translate_dict[some_list[0]] = some_list[1].split(', ')
print(translate_dict)
# eng_word = input('Введите слово для перевода: ')
# if translate_dict.get(eng_word):
# print(', '.join(translate_dict.get(eng_word)))
# else:
# print('Такого слова нет')