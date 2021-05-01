# PROBLEM 2
# Во множестве №3 найдите объекты которых нет во множестве №2
# Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

print("У нас есть первое множество")

farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2)

print("И есть второе множество")

farm_1 = {"dog", "cat", "mouse", "sheep"}
print(farm_1)

print("Надо найти объекты которые есть в первом множестве и нет во втором множестве")


print(farm_2.difference(farm_1))

print("Этих объектов нету во втором множестве")