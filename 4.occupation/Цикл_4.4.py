# 4. Напишите код, который выведет на экран список языков с нумерацией.
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# Вывод:
#  0 go
#  1 java
#  2 php
#  3 python
#  4 javascript
#  5 ruby

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for i in range(len(languages)):
		print(i, languages[i])

