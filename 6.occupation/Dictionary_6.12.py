# PROBLEM 101:
# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: 
# suitcase = [] 
# Однако он
# может вместить всего 5 вещей.
# Положите 5 вещей в чемодан.
# Вы передумали, и решили убрать последнюю вещь. 

suitcase = [] 
suitcase1 = ["Футболка", "Шорты", "Полотенце", "Плавки", "Шлёпанцы"]
suitcase.extend(suitcase1)
print(suitcase)
suitcase.remove("Шлёпанцы")
print(suitcase)