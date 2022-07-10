#Задайте список из N элементов, 
#заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях.
import random
def multyply(a,b):
 return list[a]*list[b]

n = int(input("Введите число "))
list =[]
for i in range (n):
    list.append(random.randint(-n,n))
print("Получившийся список ",list)
while True:
    a = int (input ("Введите первую позицию "))
    if a>0 and a<=n: break
while True:
    b = int (input ("Введите вторую позицию "))
    if b>0 and b<=n: break
print ("Произведение элементов на указанных позициях ", multyply(a-1,b-1)) #если считать позицию больше индекса на 1
