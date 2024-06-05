#Задание № 1

number = int(input("Введите целое число:"))

if number % 2 == 0 and number < 0: 
    print('Отрицательное четное число')
    
elif number % 2 == 0 and number > 0:
    print('Положительное четное число')
    
elif number % 2 != 0 and number < 0: 
    print('Отрицательное нечетное число')
    print('Число не является четным')
    
elif number % 2 != 0 and number > 0:
    print('Положительное нечетное число')
    print('Число не является четным')
    
else:
    print('Нулевое число')
    
#Задание №2

word = input("Введите слово: ")
vowels = ['a', 'e', 'i', 'o', 'u']

a = 0
e = 0
i = 0
o = 0
u = 0
consonants = 0


for w in word:
    if w in vowels and w == 'a':
        a += 1
    elif w in vowels and w == 'e':
        e += 1
    elif w in vowels and w == 'i':
        i += 1
    elif w in vowels and w == 'o':
        o += 1
    elif w in vowels and w == 'u':
        u += 1
    else:
        consonants += 1
            
print(f'Гласные: {a + o + e + i + u}, Cогласные: {consonants}')
if a != 0 and i != 0 and e != 0 and o != 0 and u != 0:      
    print(f"'a' = {a}, 'e' = {e}, 'i' = {i}, 'o' = {o}, 'u' = {u}") 
else:
    print(False)     
    
    
#Задание № 3

X = int(input("Минимальная сумма инвестиций: "))
A = int(input("Деньги Майкла: "))
B = int(input("Деньги Ивана: "))

if (A == B == X) or (A >= X) and (B >= X):
    print(2)
    
elif (A > B) and A >= X:
    print('Mike')
    
elif (A < B) and B >= X:
    print('Ivan')
    
elif ((A + B) >= X) and (A < X) and (B < X):
    print(1)
else:
    print(0)