#Задание №1

pets = {}

pet_name = input('Введите имя питомца: ').title()

inner_dct = dict()

for i in ['Вид питомца: ', 'Возраст питомца: ', 'Имя владельца: ']:
    data = input(i)
    inner_dct.setdefault(i.strip(': '), data)
    
x = int(list(inner_dct.values())[1])
age = ''    
inner_dct['Возраст питомца'] = x

if (x == 1) or ((x % 10 == 1) and x != 11):
    age = 'год'
elif x in range(10, 21, 1):
    age = 'лет'
elif (x in [2, 3, 4]) or ((1 < x % 10 < 5) and (x not in range(10, 21, 1))):
    age = 'года'
else:
    age = 'лет'
    
pets.setdefault(pet_name, inner_dct)

print(f"Это {list(inner_dct.values())[0]} по кличке {list(pets.keys())[0]}. Возраст питомца: {list(inner_dct.values())[1]} {age}. Имя владельца: {list(inner_dct.values())[2]}")

#Задание №2

number_dct = {}

for k in range(10, -6, -1):
    number_dct.setdefault(k, k**k)
    
print(number_dct)