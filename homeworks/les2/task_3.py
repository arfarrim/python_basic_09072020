"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
 времени года относится месяц (зима, весна, лето, осень). Напишите решения
 через list и через dict.
"""
while True:
    user_input = input("введите номер месяца")
    if user_input.isdecimal():
        break
user_input = int(user_input)
dict_month = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень", 10: "осень", 11: "осень", 12: "зима"}
print("решение через словарь - ", dict_month.get(user_input))
list_month = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
print("Решение через список - ", list_month[user_input - 1])