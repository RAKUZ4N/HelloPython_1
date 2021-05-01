# 2. Будем работать с тем же списком: 
#languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# С помощью цикла нужно “перебрать” все языки в списке, и когда код доходит до “php”, 
#цикл должен быть прерван.

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

print("У нас есть переменная которая хранит в спиcке строки")
print(languages)

print("Программа остановиться тогда когда проверка дойдёт до строки php")

for i in languages:
	
	print(i)

	if i == 'php':
		