"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями
 обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
  элементов последний сохранить на своем месте. Для заполнения списка элементов
   необходимо использовать функцию input().
"""
while True:
    user_input = input("введите элементы списка через запятую")
    if (len(user_input) > 1) or user_input.count(' ') == 0:
        break
user_list = user_input.split(",")
for itm in user_list:
    if itm[0] == " ":  # удаляем пробел после запятой
        ind_tmp = user_list.index(itm)
        itm = itm.replace(" ", "", 1)
        user_list.pop(ind_tmp)
        user_list.insert(ind_tmp, itm)
    if itm[-1] == " ":  # удаляем пробел перед запятой
        ind_tmp = user_list.index(itm)
        user_list.pop(ind_tmp)
        user_list.insert(ind_tmp, itm[0:len(itm) - 1])
out_list_ev = []
out_list_od = []
out_list = []
i = 0
for itm in user_list:
    if i % 2 == 0:
        out_list_ev.append(itm)  # список четных индексов
    if i % 2 == 1:
        out_list_od.append(itm)  # список нечетных индексов
    i += 1
i = 0
while i < (len(user_list) // 2):
    out_list.append(out_list_od[i])
    out_list.append(out_list_ev[i])
    i += 1
else:
    if (len(user_list) % 2) != 0:
        out_list.append(user_list[len(user_list) - 1])
print("список с парной перестановкой элементов\n", out_list)
