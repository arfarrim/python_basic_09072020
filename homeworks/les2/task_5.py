"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
 натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями, то новый
 элемент с тем же значением должен разместиться после них.
"""
list_rank = [7, 5, 4, 3, 1]
while True:
    user_input = input("введите новый элемент рейтинга, натуральное число")
    if user_input.isdecimal():
        break
new_rank = int(user_input)
list_rank.append(new_rank)
list_rank.sort(reverse=True)
print(list_rank)