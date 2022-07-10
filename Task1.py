#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11
def goInt(x):
  while (x%1 > 0):
    x *= 10
  return x


def sum(a):
    result = 0
    while a > 0:
        result += a % 10
        a //= 10
    return int(result)

x = float(input())
if x%1>0 :
    a = goInt(x)
else: a = x
print(f"{x} -> {sum(a)}")



