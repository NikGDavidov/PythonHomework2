#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fact(n):
 if n < 1:   
       return 1
 else:
       f = n * fact(n - 1)    
 return f

n = int(input("Введите чиcло - "))
list =[]
for i in range (n):
    list.append(fact(i+1))
print(f"N = {n} ->{list}")



