a = int( input("Введите число начала диапазона: ") )
b = int( input("Введите число конца диапазона: ") ) + 1
print ("Четные числа:") 
[ print(num, end = " ") for num in range(a,b) if a < b and num % 2 == 0]
