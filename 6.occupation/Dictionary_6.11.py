# PROBLEM 11:
# Есть список Южноамериканских стран
# СПИСОК №2
# в котором Суринам встречается два раза. Необходимо написать программу,
# которая удалит дублирующуюся запись, и возвратит в результате список.
# Список № 2
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 
# 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 
'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
south_american_countries.remove('Suriname')
print(south_american_countries)