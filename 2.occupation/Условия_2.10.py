# PROBLEM 33:
# Напишите условие, которое выводит отрицательные числа

numbers = int(input("Введите число: "))

if numbers < 0:
	print("Ваше число отрицательное", numbers)

elif numbers == 0:
	print("Ошибка! Вы ввели число 0")

else:
	print("Ошибка! Вы ввели положительное число", numbers)
