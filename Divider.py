# -*- coding: cp1251 -*-
x = int(input("Ââåäèòå ÷èñëî X: "))
if x == 1:
     d = 1
else:
    d = 2
for i in range(2, int((x/2) + 1)):
    if x % i == 0:
      d += 1
print(d)
