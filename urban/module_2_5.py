def get_matrix(n, m, value):
    matrix = []                      # создаем пустой список для матрицы
    if n <= 0 or m <= 0:
        return matrix                # возвращаем пустой список, если n или m меньше, или равно 0
    for i in range(n):               # внешний цикл для строк
        matrix.append([])            # добавляем пустой список для новой строки
        for j in range(m):           # внутренний цикл для столбцов
            matrix[i].append(value)  # заполняем ячейку строки значением value
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
