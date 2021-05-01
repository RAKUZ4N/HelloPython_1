# PROBLEM 15:
# Есть три числа 17391, 546, 934.
# Если каждое из них поделить на 17 по модулю, где остаток меньше всего? 

number1 = 17391
print("Первое число -", number1)

number2 = 546
print("Второе число -", number2)

number3 = 934
print("Третье число -", number3)

remainder1 = 17391 % 17
print("Остаток первого числа:", remainder1)

remainder2 = 546 % 17
print("Остаток второго числа:", remainder2)

remainder3 = 934 % 17
print("Остаток третьего числа:", remainder3)

if remainder1 < remainder2 and remainder1 < remainder3:
	print("У первого числа остаток меньше всего")

elif remainder2 < remainder1 and remainder2 < remainder3:
	print("У второго числа остаток меньше всего")

elif remainder3 < remainder1 and remainder3 < remainder2: 
	print("У третьего числа остаток меньше всего")

else: 
	print("Остатки трёх чисел равны к друг другу!")