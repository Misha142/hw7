def print_operation_table(operation, num_rows=6, num_columns=6):
    
    print(*[[operation(x,y) for x in range(1,num_columns+1)] for y in range(1,num_rows+1)],sep='\n')     #не до конца понял как нормальный вывод сделать в 1 строку тут
    print()
    
    matrix=[[operation(x,y) for x in range(1,num_columns+1)] for y in range(1,num_rows+1)]
    for col in matrix:
        for row in col:
            print(str(row).rjust(3),end=' ')
        print()                                       # вывод покрасивее
        
    
        
print_operation_table(lambda x, y: x * y ,10, 15)