# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = int(input("Задайте число: "))

fib1 = 1
fib2 = -1
  
print(fib1, fib2, end=' ')
 
for i in range(-1, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

fib3 = fib4 = 1

print(fib3, fib4, end=' ')
 
for i in range(2, n):
    fib3, fib4 = fib4, fib3 + fib4
    print(fib4, end=' ')