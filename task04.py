# Напишите функцию для транспонирования матрицы
matrix = [[123, 234, 456],
          [678, 890, 123],
          [345, 567],
          [987, 765, 543]]


def transporing_matrix(mat):
    new_mat = []
    for i in range(0, len(mat) - 1):
        new_row = []
        for old_row in mat:
            try:
                new_row.append(old_row[i])
            except:
                new_row.append(None)
        new_mat.append(new_row)
    return new_mat


print(transporing_matrix(matrix))
