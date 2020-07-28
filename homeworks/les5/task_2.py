"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os
file_path = os.path.join(os.path.dirname(__file__), "task_2")
with open(file_path, "r", encoding="UTF-8") as file:
    file_dump = file.read()
    end_mark = file.tell()
    line_count = 1
    word_count = 1
    for itm in file_dump:
        if itm == " ":
            word_count += 1
        if itm == "\n":
            line_count += 1
            print(f"длина {line_count - 1} строки - {word_count} слов")
            word_count = 1
    else:
        print(f"длина {line_count} строки - {word_count} слов")
    print(f'Количество строк в файле = {line_count}')
