import random

matrix_1 = []
matrix_2 = []

strokes = int(input("Кол-во строк: "))
columns = int(input("Кол-во столбцов: "))


for x in range(strokes):
    matrix_1.append([random.randint(-100, 100) for i in range(columns)])
    matrix_2.append([random.randint(-100, 100) for i in range(columns)])
        

def addition(a, b):
    
    matrix_c = []
    for x in range(len(a)):
        lst = []
        for y in range(len(a[x])):
            lst.append(a[x][y] + b[x][y])
                
        matrix_c.append(lst)
            
    return(matrix_c)
    
print("Результирующая матрица: ")
print(*addition(matrix_1, matrix_2), sep='\n')