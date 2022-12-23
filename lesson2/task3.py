# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random
def mix_list(list_orig):
     list = list_orig[:]
     list_length = len(list)
     for n in range(list_length):
         index_unknow = random.randint(0, list_length-1)
         temp = list[n]
         list[n] = list[index_unknow]
         list[index_unknow] = temp
     return list
list = [1, 2, 5, 4, 0, 6, 9, 8, 3]
mixed_list = mix_list(list)
print(f"исходный список: {list}")
print(f"перемешанный список: {mixed_list}")