# 1. Допустим у нас есть список языков программирования. lang1 = 'Rust'
#  languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#  Обязательное условие: если переменная в списке, то нужно вывести на экран 'this languages is in list'. 
#  Если этого языка нет в списке, ничего не нужно выводить.

lang1 = "Rust"
print("Первая переменная:", lang1)

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
print("Вторая переменная:", languages)

for i in languages:
	print(i)
	if i == lang1:
		print('this languages is in list')

	print(" ")