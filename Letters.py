# -*- coding: cp1251 -*-
word = input("������� ����� ����� �� ��������� ����� ���������� �������: ")
list = ['a','o','i','u','e']
glas = 0
sogl = 0
for i in range(len(word)):
    if word[i] in list:
      glas += 1
else:
    sogl += 1
print("���������� ������� ����: ", glas)
print("���������� ���������: ", sogl)
