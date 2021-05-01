# PROBLEM 31:
# Создайте пустой словарь.
# Запустите цикл который 3 раза спросит его имя и его пароль.
# Записывайте имя пользователя как ключ, а пароль как его значение.

login_password = {}

for i in range(3):
	login = input("Введите ваш логин: ")
	password = input("Введите ваш пароль: ")
	login_password[login] = password
	print(login_password)