"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При
нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод
чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""


def inc_num_sec():
    """Накапливает сумму введенных через пробел чисел до ввода спец символа "@".

    """
    sum_glob = 0  # хранит сумму чисел всех итераций ввода
    repeat_mark = 1  # метка повторения ввода
    while repeat_mark == 1:
        user_str = input("введите числа разделенные пробелом,\nдобавьте @ чтобы закончить")
        if "@" in user_str:  # поиск спец символа останова
            user_str = user_str.replace("@", "")
            repeat_mark = 0
        if user_str != "":  # обработка пустой строки
            user_str = user_str.split(" ")
            for itm in user_str:
                sum_glob += int(itm)
        if repeat_mark == 0:
            print("конечная сумма чисел = ", sum_glob)
            continue
        print("сумма чисел на последнем шаге = ", sum_glob)
inc_num_sec()
