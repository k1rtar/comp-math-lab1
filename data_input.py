def read_from_file(filename):
    with open(filename, 'r') as file:
        size = int(file.readline())
        matrix = []
        for _ in range(size):
            row = [float(num.replace(',', '.')) for num in file.readline().split()]
            if len(row) != size:
                raise ValueError("Количество элементов в строке матрицы не совпадает с размерностью матрицы")
            matrix.append(row)
        vector = [float(num.replace(',', '.')) for num in file.readline().split()]
        if len(vector) != size:
            raise ValueError("Размерность вектора не совпадает с размерностью матрицы")
        precision = float(file.readline().replace(',', '.'))
    return matrix, vector, precision

def read_from_keyboard():
    size = int(input("Введите размер матрицы: "))
    print("Введите матрицу построчно:")
    matrix = []
    for _ in range(size):
        row = [float(num.replace(',', '.')) for num in input().split()]
        if len(row) != size:
            raise ValueError("Количество элементов в строке матрицы не совпадает с размерностью матрицы")
        matrix.append(row)
    print("Введите вектор:")
    vector = [float(num.replace(',', '.')) for num in input().split()]
    if len(vector) != size:
        raise ValueError("Размерность вектора не совпадает с размерностью матрицы")
    precision = float(input("Введите точность: ").replace(',', '.'))
    return matrix, vector, precision


