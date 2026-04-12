def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    output = []

    for j in range(columns):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        output.append(new_row)
    
    return output

a = [[9, 7, 8], 
     [4, 5, 2]]

print(f"*** -TRANSPOSING_MATRIX...- ***\n\nTransposed matrix = {transpose(a)}")