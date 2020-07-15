"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список
 кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно
 быть два элемента — номер товара и словарь с параметрами (характеристиками
 товара: название, цена, количество, единица измерения). Структуру нужно сформировать
 программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
ключ — характеристика товара, например название, а значение — список
значений-характеристик, например список названий товаров.
"""
item_list = []  # список товаров, строка - № + словарь параметров
item_index = 1
while True:
    user_add = input("Добавить товар в список? да/нет")  # запрос добавления строки
    if user_add.lower() == "да":
        new_title = {}
        user_input = input("введите название товара")  # заполнения словаря дял текущей строки
        new_title.update({"название": user_input})
        user_input = input("введите цену товара")
        new_title.update({"цена": user_input})
        user_input = input("введите колличество товара")
        new_title.update({"колличество": user_input})
        user_input = input("введите единицу измерения товара")
        new_title.update({"единица измерения": user_input})
        new_title_tup = (item_index, new_title)  # формирование строки
        item_list.append(new_title_tup)  # добавление строки в структуру(список товаров)
        item_index += 1
    elif user_add.lower() == "нет":
        break
print("Сформирован список товаров\n", item_list)
base_name = []  # инициализация списков для заполнения базы товаров
base_price = []
base_quant = []
base_uom = []
item_base = {}
for itm in item_list:
    base_name.append(itm[1].get("название"))  # заполнение базы товаров
    base_price.append(itm[1].get("цена"))
    base_quant.append(itm[1].get("колличество"))
    base_uom.append(itm[1].get("единица измерения"))
item_base.update({"название": base_name})
item_base.update({"цена": base_price})
item_base.update({"колличество": base_quant})
item_base.update({"единица измерения": base_uom})
print("Сформирована база товаров\n", item_base)
