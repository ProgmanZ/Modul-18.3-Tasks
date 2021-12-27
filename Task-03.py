# Задача 3. Разделители символов

user_template = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
# 'С днём рождения, {name}! С {age}-летием тебя!
congr_people = input('Список людей через запятую: ').split(', ')

# Иван Иванов, Петя Петров, Лена Ленова
age_list = input('Возраст людей через пробел: ').split(' ')
# 20 30 18

age_list = [int(i) for i in age_list]

for i in range(len(congr_people)):
    print(user_template.format(name=congr_people[i], age=str(age_list[i])))

birthdays = ['{name} {age}'.format(name=congr_people[i], age=age_list[i]) for i in range(len(congr_people))]
print('Именинники:', ', '.join(birthdays))
