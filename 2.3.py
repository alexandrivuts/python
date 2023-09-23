def find_min_index(matrix):
    min_value = matrix[0][0]
    min_row, min_col = 0, 0

    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_row = row_index
                min_col = col_index

    return min_row+1, min_col+1

def find_max_index(matrix):
    max_value = matrix[0][0]
    max_row, max_col = 0, 0  

    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_row, max_col = row_index, col_index

    return max_row+1, max_col+1

matrix = [
    [4, 9, 3],
    [2, 7, 1],
    [9, 5, 6]
]
max_row, max_col = find_max_index(matrix)
min_row, min_col = find_min_index(matrix)
print(f"Индексы первого вхождения минимального элемента: ({min_row}, {min_col})")
print(f"Индексы максимального элемента в матрице: ({max_row}, {max_col})")
