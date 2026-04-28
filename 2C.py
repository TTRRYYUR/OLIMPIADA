def input_matrix() -> list[list[int]]:
    """Функция для ввода квадратной матрицы"""
    n = int(input("Введите размер квадратной матрицы n: "))
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"A[{i}][{j}] = "))
            row.append(element)
        matrix.append(row)
    return matrix


def print_matrix(matrix, width=6) -> None:
    """Вывод с выравниванием влево"""
    for row in matrix:
        print(''.join(f"{x:<{width}}" for x in row))

def swap_elements(matrix) -> None:
    """ """
    pass


def create_vector(matrix) -> list:
    """Функция для формирование вектора B"""
    B = []
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum += element
        B.append(row_sum)
    return B


A = input_matrix()
if len(A) == 0:
    print("Матрица А пустая!!!")
else:
    swap_elements(A)
    print_matrix(A)
    B = create_vector(A)
    print(B)
