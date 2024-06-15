#Задание №1

lst = []

for n in range(int(input('Введите число: '))):
    lst.append(input('Число, которое будет добавлено в список: '))


print(*lst[::-1], sep=' ')

# print(lst.reverse())


#Задание №2

N = int(input('Введите число от 1 до 10000: '))

array = input('Введите числа: ').split()


for i in range(N, 0, -1):
    
    array[i - 1] = array[i - 2]
        
array[0] = N
   
print(*array, sep=' ')


#Задание №3

m = int(input("Максимальный вес для одной лодки: "))

weights = []
n = int(input("Количество рыбаков: "))

for i in range(n):
    weights.append(int(input(f'Вес {n - (n - i - 1)}: ')))

count = 0
weights.sort()

if (n == 1) and (n <= m):
    print('Понадобится одна лодка')
    
else:    
    for w in range(0, len(weights) - 1, 2):
        
        if (weights[w] + weights[w + 1] <= m) and (len(weights) - 2) != 1:
            count +=1
            
        #уловие для списка из трех человек    
        elif (weights[w] + weights[w + 1] <= m) and (len(weights) - 2) == 1:
            count += 2
            break
        
        elif all(map(lambda x: x > m, weights)):
            count = 0
            break
        
        else:
            count += len(weights[w:])
            break
            
                
if (str(count)[-1] == '1') and ((count > 20) or (count == 1)):
    print(f"Понадобится {count} лодка")
    
elif (str(count)[-1] in ['2', '3', '4']) and ((count > 20) or (1 < count < 5)):
    print(f"Понадобится {count} лодки")
  
elif count == 0:
    print('Ни один рыбак не поместился в лодку') 
    
else:
    print(f"Понадобится {count} лодок")
    
print(weights)