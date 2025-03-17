# -*- coding: cp1251 -*-
n=int(input("Введите количество чисел "))
a=0
for i in range(n):
    s=int(input("введите целое число "))
    if s==0:
        a+=1
print("Вы ввели ноль", a, "количества раз")



