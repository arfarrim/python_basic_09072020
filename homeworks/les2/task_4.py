"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в
слово длинное, выводить только первые 10 букв в слове.
"""
user_input = input("Введите слова, разделенные пробелами")
user_list = user_input.split(" ")
for ind, el in enumerate(user_list, 1):
    print(ind, el[0:9])
