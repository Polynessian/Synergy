#Задание №1

n = int(input("Целое число "))

lst = []
for i in range(n):
    lst.append(int(input(f"Целые числа {n - i} раз ")))
    
res = lst.count(0)

print(res)


#Задание №2

X = int(input("Введите целое число: "))

if X <= 2000000000:
    cnt = 0
    for i in range(1, X + 1):
        if X % i == 0:
            cnt += 1
    print(cnt)
else:
    raise Exception('Слишком большое число')       

#Задание №3

A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

if A <= B:
    lst = []
    
    for i in range(A, B+1):
        if i % 2 == 0:
            lst.append(i)
    print(*lst, sep=' ')
    
else:
    raise Exception("Число А должно быть меньше/равно B")