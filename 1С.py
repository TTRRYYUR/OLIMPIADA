def input_arr(n) -> list:
    """Функция для ввода массива"""
    arr = []
    for i in range(n):
        numbers = int(input(f"arr[{i}] = "))
        arr.append(numbers)
    return arr


def sum_even_numbers(arr) -> int:
    """Функция для суммы всех четных элементов в массиве"""
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total


def search_negatives(arr) -> list:
    """Функция для поиска всех отрицательных чисел в массиве"""
    negatives_numbers = []
    for num in arr:
        if num < 0:
            negatives_numbers.append(num)
    return negatives_numbers


def search_max(arr) -> int:
    """Функция для поиска максимального значения в массиве"""
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def bubble_sort_abs(arr) -> None:
    """Функция для сортировки массива по возрастанию модуля"""
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if abs(arr[j]) > abs(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def deleted_numbers(arr, k) -> list:
    """Функция для удаления элемента из массива"""
    result = []
    for num in arr:
        if num != k:
            result.append(num)
    return result


n = int(input("Введите размер массива X"))
X = input_arr(n)
print(X)

if len(X) == 0:
    print("Пустой массив X!!!")
else:
    sum_even = sum_even_numbers(X)
    print(sum_even)
    list_negatives = search_negatives(X)
    if len(list_negatives):
        max_of_negatives = search_max(list_negatives)
        print(max_of_negatives)
    else:
        print("Нет отрицательных элементов")
    m = int(input("Введите размер массива Y"))
    Y = input_arr(m)
    if len(Y) == 0:
        print("Пустой массив Y!!!")
    else:
        Z = X + Y
        print(Z)
        bubble_sort_abs(Z)
        print(Z)
        k = int(input("Введите число которое нужно удалить"))
        Z = deleted_numbers(Z, k)
        print(Z)


# n = int(input("Введите размер массива Х"))
# m = int(input("Введите размер массива Y"))
#
# X = input_arr(n)
# Y = input_arr(m)
# if len(X) == 0:
#     print("Массив должны быть не пустыми!!!")
# elif len(Y) == 0:
#     print("Массив должны быть не пустыми!!!")
# else:
#     sum_even = sum_even_numbers(X)
#     print(sum_even)
#     list_negatives = search_negatives(X)
#     if len(list_negatives):
#         max_of_negatives = search_max(list_negatives)
#         print(max_of_negatives)
#     else:
#         print("Нет отрицательных элементов")
#     Z = X + Y
#     print(Z)
#     bubble_sort_abs(Z)
#     print(Z)
#     k = int(input("Введите какое число нужно удалить"))
#     Z = deleted_numbers(Z, k)
#     print(Z)
