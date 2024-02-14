from solver import Solver
from matrix_generator import generate_random_matrix
from data_input import read_from_file, read_from_keyboard

def main():
    
    choice = input("Введите 'f' для чтения из файла, 'k' для ввода с клавиатуры, 'r' для генерации случайной матрицы: ")
    if choice == 'f':
        filename = input("Введите имя файла: ")
        try:
            matrix, vector, precision = read_from_file(filename)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return
    elif choice == 'k':
        try:
            matrix, vector, precision = read_from_keyboard()
        except Exception as e:
            print(f"Ошибка при вводе данных: {e}")
            return
    elif choice == 'r':
        size = int(input("Введите размер матрицы: "))
        matrix, vector = generate_random_matrix(size)
        precision = float(input("Введите точность: ").replace(',', '.'))
    else:
        print("Неверный выбор.")
        return
    print("Исходная матрица: ")
    for v in matrix: print(v)
    solver = Solver(matrix, vector, precision)
    solution_vector, iteration_count, residuals = solver.solve()
    if choice=='f' or choice == 'r':
        print("Исходная матрица: ")
        for v in matrix: print(v)
        print("Исходный вектор: ",v)
    if solution_vector is None:
        print(iteration_count)
    else:
        print("Вектор решений: ")
        for x in solution_vector: print(x)
        print("Количество итераций: ", iteration_count)
        print("Вектор погрешностей: ", residuals)

if __name__ == "__main__":
    main()
