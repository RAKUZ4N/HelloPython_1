# PROBLEM 3
# Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.
# А затем удалите через .pop() элемент и посмотрите что же вы удалили.

print("Создаём SET из 5 элементов")
elements = {"Attack on Titan", "Naruto", "Kimi no na wa", "Koe no Katachi", "Bleach"}
print(elements)

print("Потом добавляем в SET ещё один элемент")
elements.add("Demon Slayer")
print(elements)

print("И рандомно удаляем один элемент")
elements.pop()
print(elements)