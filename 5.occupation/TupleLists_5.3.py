# PROBLEM 11
# Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.

print("Создать список и заполнить 5 разными типами данных")

list1 = ["str", 99, 85.15, True, [" "]]
list2 = []

print("Создаём пусток список")

list2.extend(list1)

print("и через метод extend переносим первый список во второй пустой список")

print(list2)