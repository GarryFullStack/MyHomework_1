# -*- coding: cp1251 -*-
word = input("Введите любое слово на латинском языке маленькими буквами: ")
list = ['a','o','i','u','e']
glas = 0
sogl = 0
for i in range(len(word)):
    if word[i] in list:
      glas += 1
else:
    sogl += 1
print("Количество гласных букв: ", glas)
print("Количество согласных: ", sogl)
