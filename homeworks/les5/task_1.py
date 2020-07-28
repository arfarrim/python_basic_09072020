"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
import os
file_name = os.path.join(os.path.dirname(__file__), 'task_1')
with open(file_name, "w", encoding="UTF-8") as file:
    mark = 1
    while mark:
        user_input = input("Введите новую строку для записи в файл\nлибо оставьте поле пустым"
                           " и нажмите enter для завершения")
        if user_input == "":
            mark = 0
            break
        file.writelines(user_input + "\n")
