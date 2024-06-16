#Задание №1

N = int(input('Введите целое число: '))
lst = input(f'Введите {N} чисел через пробел: ').split()[:N]
print(lst)

U = set(int(x) for x in lst)
print(f"Кол-во различных чисел: {len(U)}")

#Задание №2

array_1 = set(map(int, input('Введите первый список чисел через пробел: ').split()))
array_2 = set(map(int, input('Введите второй список чисел через пробел: ').split()))
  
print(f"Кол-во чисел на пересечении множеств: {len(array_1 & array_2)}", sep='\n')

#Задание №3

subsequence = map(int, input('Введите последовательность чисел через пробел: ').split())

subset = set()

for s in subsequence:
    if s not in subset:
        print('NO')
        subset.add(s)
    else:
        print('YES')