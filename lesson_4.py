#Задание №
side_one = input("Введите размер первой стороны:")
side_two = input("Введите размер второй стороны:")

if '.' in side_one:
    side_one = float(side_one)
else:
    side_one = int(side_one)
    
if '.' in side_two:
    side_two = float(side_two)
else:
    side_two = int(side_two)
    
    
square = side_one * side_two
perimeter = side_one + side_two

print(f'Площадь = {square}, Периметр = {perimeter}')

#Задание №2
number = int(input("Введите пятизначное число:"))

number_of_units = number % 10
number_of_tens = str(number % 100)[:1]

res1 = int(number_of_tens) ** number_of_units

number_of_hundreds = str(number % 1000)[:1]

res2 = res1 * int(number_of_hundreds)

number_of_thousands = str(number % 10000)[:1]
number_of_tensthousand = str(number % 100000)[:1]

res3 = res2 / (int(number_of_tensthousand) - int(number_of_thousands))

print(res3)