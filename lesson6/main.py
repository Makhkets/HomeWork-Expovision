matrix = [

         [1, 2, 3, 4, 5, 6, 7, 8],
         [8, 7, 6, 5, 4, 3, 2, 1],
         [2, 3, 4, 5, 6, 7, 8, 9],
         [2, 2, 2, 6, 2, 4, 6, 2],
         [1, 3, 5, 7, 9, 7, 5, 3],
         [3, 1, 5, 3, 2, 6, 5, 7],
         [1, 7, 5, 9, 7, 3, 1, 5],
         [2, 6, 3, 25, 1, 7, 3, 2]

]

# Напишите функцию возведения всех элементов матрицы в квадрат. И красивый вывод списка
def square(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] **= 2

    for i in matrix:
        text = ""
        for j in i:
            if len(str(j)) > 1:
                text += f"{j}   "
            elif len(str(j)) <= 1:
                text += f"{j}    "

        print(text)

    return matrix

# Напишите функцию возведения всех четных элементов в квадрат.
def square_even(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j%2==0:
                matrix[i][j] **= 2

    for i in matrix:
        text = ""
        for j in i:
            if len(str(j)) > 1:
                text += f"{j}   "
            elif len(str(j)) <= 1:
                text += f"{j}    "

        print(text)

    return matrix

# Напишите функцию возведения в квадрат всех элементов меньше 5.
def square_five(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < 5:
                matrix[i][j] **= 2

    for i in matrix:
        text = ""
        for j in i:
            if len(str(j)) > 1:
                text += f"{j}   "
            elif len(str(j)) <= 1:
                text += f"{j}    "

        print(text)

    return matrix

# Напишите функцию возведения первых четырех строк в квадрат.
def square_first4(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if count == 4:
                break
            else:
                matrix[i][j] **= 2
                count += 1

    for i in matrix:
        text = ""
        for j in i:
            if len(str(j)) > 1:
                text += f"{j}   "
            elif len(str(j)) <= 1:
                text += f"{j}    "

        print(text)

    return matrix

# Напишите функцию сложения по строкам.
def string_addition(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            text += str(matrix[i][j])
        text += "\n"

    print(text)
    return matrix

# Напишите функцию сложения по столбцам.
def ddition_by_columns(matrix):
    result = []
    for i in range(len(matrix)):
        sum_string = []
        for j in range(len(matrix[i])):
            sum_string.append(matrix[i][j])
        result.append(sum(sum_string))

    for i in result:
        print(i)

    return matrix

# Напишите функцию сложения по строкам четных элементов.
def string_addition_even(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if int(matrix[i][j])%2==0:
                text += str(matrix[i][j])
        text += "\n"

    print(text)
    return matrix

# Напишите функцию сложения по столбцам четных элементов.
def sum_even_number_list(matrix):
    result = []
    for i in range(len(matrix)):
        sum_string = []
        for j in range(len(matrix[i])):
            if int((matrix[i][j]))%2==0:
                sum_string.append(matrix[i][j])
        result.append(sum(sum_string))

    for i in result:
        print(i)

    return matrix

# Напишите функцию возведения в квадрат всех элементов четныхстолбцом.
def sum_even_number_list_end(matrix):
    result = []
    for i in range(len(matrix)):
        sum_string = []
        for j in range(len(matrix[i])):
            if int((matrix[i][j]))%2==0:
                sum_string.append(matrix[i][j])
            else:
                sum_string = []
                break

        result.append(sum(sum_string))

    for i in result:
        print(i)

    return matrix

# Напишите функцию возведения в квадрат всех элементов четныхстолбцом.
def square_all_elemetns_even(matrix):
    result = []
    new_result = []
    for i in range(len(matrix)):
        sum_string = []
        for j in range(len(matrix[i])):
            if int((matrix[i][j]))%2==0:
                sum_string.append(matrix[i][j])
            else:
                sum_string = []
                break

        result.append(sum(sum_string))

    for i in result:
        new_result.append(i**2)

    for i in new_result:
        print(i)
    return new_result

def row_multiplication(matrix):
    result = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += str(matrix[i][j]) * len(str(matrix[i][j]))


    print(result)
    return matrix

# Напишите функцию сложения всех элементов матрицы.
def square_all_elements(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += matrix[i][j]

    print(result)
    return result

# Напишите функцию сложения всех элементов матрицы меньших 5 (в одно число) и всех элементов матрицы больше или равных 5 (в другое число). Сравните числа и выведите, какое из них больше.
def square_all_elements_menshe5(matrix):
    result = 0
    findMaxNumber = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] <= 5:
                result += matrix[i][j]
                findMaxNumber.append(matrix[i][j])

    print(max(findMaxNumber))
    return result

# Напишите функцию замены значений всех элементов матрицы на 0.
def replace_all_elements(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0

    for i in matrix:
        text = ""
        for j in i:
            if len(str(j)) > 1:
                text += f"{j}   "
            elif len(str(j)) <= 1:
                text += f"{j}    "

        print(text)

    return matrix

# Пользователь вводит через консоль число. Напишите функцию, которая заменит все числа в матрице, которые меньше введенного, на введенное число.
def replace_all_elements_x(matrix):
    x = int(input())
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < x:
                matrix[i][j] = x

    for i in matrix:
        text = ""
        for j in i:
            if len(str(j)) > 1:
                text += f"{j}   "
            elif len(str(j)) <= 1:
                text += f"{j}    "

        print(text)

    return matrix

# Напишите функцию возведения всех чисел 5 в квадрат.
def replace_all_elements_5(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 5:
                matrix[i][j] **= 2

    for i in matrix:
            text = ""
            for j in i:
                if len(str(j)) > 1:
                    text += f"{j}   "
                elif len(str(j)) <= 1:
                    text += f"{j}    "

            print(text)

    return matrix

# Напишите функцию, которая удалит 4 последних строки.
def row_multiplication_last5(matrix):
    result = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += str(matrix[j][i])

        result += "\n"

    new_result = []
    result = result.split("\n")
    for i in result[:4]:
        print(i)
        new_result.append(i)


    return new_result

# Пусть пользователь через консоль вводит число. Напишите функцию удаления строки в матрице, чей номер равен введенному числу.q
def delete_string(matrix):
    result = ""
    line = input()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += str(matrix[j][i])

        result += "\n"

    new_result = []
    result = result.split("\n")
    for i in result:
        print(i)
        if line in i:
            pass
        else:
            new_result.append(i)

    print(new_result)

    return result

# Пусть пользователь через консоль вводит число. Напишите функцию удаления столбца в матрице, чей номер равен введенному числу.
def delete_number_(matrix):
    result = ""
    number = input("Введите номер: ")
    matrix[int(number)] = []
    print(matrix)
    return matrix

# Напишите функцию очистки матрицы.
def clear_matrix(matrix):
    for i in range(len(matrix)):
        matrix[i] = []

    print(matrix)
    return matrix

# Напишите функцию, которая поменяет первый и последний столбцы матрицы местами.
def clear_matrix(matrix):
    new = matrix[-1]
    matrix[-1] = matrix[0]
    matrix[0] = new

    print(matrix)

    return matrix

