# -*- coding: cp1251 -*-
print("������� ����������� ����� ����������:")
minInv = int(input())
print("������� ��������� ����� ��� ���������� � �����:")
invIvan = int(input())
print("������� ��������� ����� ��� ���������� � ������:")
invMike = int(input())

sumInv = invIvan + invMike
print("����� ����� ����������: ", sumInv)

if (invIvan >= minInv) and (invMike >= minInv):
    print("2")
elif (invIvan >= minInv) and (invMike <= minInv):
    print("Ivan")
elif (invIvan <= minInv) and (invMike >= minInv):
    print("Mike")
elif sumInv >= minInv:
    print("1")
else: 
    print("0")

