# Problem 2:
# Спросить у пользователя символ и поделить строку №4 по этому символу. 
# Строка №4:
# 'GitHub'

varString = "GitHub"

print("Надо поделить эту строку, присутствующими буквами в строке:", varString)

string = input("Введите символ: ")

print("Ваш введённый символ:", string)

print(string.join(varString))