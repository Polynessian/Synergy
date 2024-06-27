# Задание №1

def find_f(N):
    f = list(range(N))[1:]
    f.append(N)
    
    res = 1
    for cnt in f:
        res *= cnt 
    
    return res
    
    
data = int(input('Введите натуральное целое число: '))
result_list = []

for i in range(find_f(data), 0, -1):
    result_list.append(find_f(i))
    
print(result_list)
    
# Задание № 2

import collections


pets = {}

def get_pet(ID):
    if ID in pets.keys():
        return dict(pets[ID])
    else:
        return False

def create():
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
    else:
        last = 1
    
    pet_name = input('Введите имя питомца: ').title()
    
    middle_dct = {}
    inner_dct = dict()

    for i in ['Вид питомца: ', 'Возраст питомца: ', 'Имя владельца: ']:
        s = input(i)
        inner_dct.setdefault(i.strip(': '), s)
    
    middle_dct.setdefault(pet_name, inner_dct)
    if pets:
        pets.setdefault(last + 1, middle_dct)
    else:
        pets.setdefault(last, middle_dct)

def get_suffix(age):
    
    suffix = ''
    
    if (age == 1) or ((age % 10 == 1) and age != 11):
        suffix = 'год'
    
    elif age in range(10, 21, 1):
        suffix = 'лет'
        
    elif (age in [2, 3, 4]) or ((1 < age % 10 < 5) and (age not in range(10, 21, 1))):
        suffix = 'года'
        
    else:
        suffix = 'лет'
        
    return suffix       

def read():
    data = int(input("Введите ID питомца: "))
    if get_pet(data):
        for k, v in get_pet(data).items():
            
            print(f"Это {v['Вид питомца']} по кличке '{k}'. Возраст питомца: {v['Возраст питомца']} {get_suffix(int(v['Возраст питомца']))}. Имя владельца: {v['Имя владельца']}")
            break
    else:
        print("Питомца с таким ID нет в базе данных")
def update():
    
    pet = int(input("Введите ID питомца: "))
    
        
    if get_pet(pet):
         
        for i in ['Вид питомца: ', 'Возраст питомца: ', 'Имя владельца: ']:
            s = input(i)
            for k in get_pet(pet).keys():
                pets[pet][k][i.strip(': ')] = s
                
        print("Успешно изменено")
    else:
        print("Питомца с таким ID нет в базе данных")

def delete(data):
    del pets[data]



def pets_list():
    for k, v in pets.items():
        print(f"{k} : {v}")
    
        
while True:
    
    command = input("Доступные команды: create - создать запись\n \
        read - вывести запись о питомце\n \
        print - вывести список питомцев в терминал\n \
        delete - удалить запись по ID\n \
        stop - выход из программы\n \
        Введите команду: ")
              
    while command != "stop":
           
        if command == 'create':
            create()
        
        elif command == 'update':
            update()
            
        elif command == 'delete':
            data = int(input('Введите ID питомца для удаления: '))
            if get_pet(data):
                delete(data)
                print("Удалено")
            else:
                print("Питомца с таким ID нет в базе данных")
        
        elif command == 'read':
            read()
            
        elif command == 'print':
            pets_list()
            
        else:
            print("Команда не распознана")
            
        command = input("Введите команду: ")
    
    if command == "stop":
        break
    else:
        continue
    
