# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


# num = input("Введите вещественное число: ")

# def sum_num(num):
#     return sum(map(int, num.replace(".","").replace("-","")))

# print(f"Сумма цифр в этом числе равна {sum_num(num)}")

num = input("Введите вещественное число: ")
sum_num = lambda sum_num: sum(map(int, num.replace(".","").replace(",","")))
print(f"Сумма цифр в этом числе равна {sum_num(num)}")