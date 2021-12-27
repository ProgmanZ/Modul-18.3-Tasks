# Задача 1. Улучшенная лингвистика 2

search_word = input('Введите слова для поиска: ').split()
text = input('Введите текст в котором необходимо найти слова: ').split()

count_list = []

for n in range(len(search_word)):
    count_list.append(text.count(search_word[n]))
    print('Слово {0} в тексте встречается {1} раз'.format(search_word[n], count_list[n]))


