#Задание №1

res1 = input('Введите название питомца:')
res2 = input('Введите кличку:')
res3 = input('Введите возраст:')

print(f'Это {res1} по кличке "{res2}". Возраст: {res3} года')

#Задание №2

lst = []

for i in range(6):
    buffer = input(f'Стадия номер {i + 1}:')
    lst.append(buffer)
    
print(*lst, sep="=>")