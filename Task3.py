#Задайте список из n чисел последовательности  (1 + 1/n)^n и выведите на экран их сумму.

#Пример:

#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def func(n):
 
 return (1+1/n)**n

n = int(input("Введите чиcло - "))
list =[]
sum =0
for i in range (n):
   list.append(func(i+1))
   sum += list[-1]
print(f"N = {n} ->{list}")
print (f"Сумма последовательности - {sum}")



