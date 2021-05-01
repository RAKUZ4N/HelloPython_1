# PROBLEM 020:
# Создайте SET который хранит в себе все методы  для работы  с  SET.
# Создайте второй SET который хранит в себе  методы  для работы  с  Dictionary которые вы сегодня узнали.
# Проверьте какие методы похожи у этих типов данные.

set_methods = {"add", "remove", "clear", "update", "difference", 
"discard", "intersection", "intersection_update", "pop"}

dictionary_methods = {"clear", "keys", "items", "get", "values", "update"}

print(set_methods.intersection(dictionary_methods))