#Реализуйте алгоритм перемешивания списка.

import random
def mix (list:list):
    for i in range (len (list)-2):
        j = random.randint(i,len(list)-1)
        temp = list[i]
        list[i]=list[j]
        list [j]= temp
    return list


n = int(input("Введите число элементов списка"))
list =[]
for i in range (n):
    list.append(random.randint(-n,n))
print("Получившийся список ",list)
list2 = mix(list)
print ("Перемешанный список -> ", list2)
