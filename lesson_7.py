#Задание №1

data = input('Введите слово: ')

if data == data[::-1]:
    print("yes")
else:
    print("no")


#Задание №2

row = 'i   f   f ghjj  h'
        
while '  ' in row:
    row = row.replace('  ', ' ', 1)
    
print(row, row.count(' '))
