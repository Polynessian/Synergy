my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def req(sequence, idx=0):
    
    while len(sequence) != idx:
        x = sequence[idx]
        return str(x)+ ' ' + str(req(sequence, idx + 1))
    
    return "Конец списка"
    
    
    
print(req(my_list))