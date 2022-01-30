import random
import math


def generate_binary_file(file_size, file_name):
    generic_string = ""
    for _ in range(file_size):
        generic_string += random.randint(0, 1).__str__()
    file = open(f'source/{file_name}.txt', 'w')
    file.write(generic_string)
    file.close()


def frequency_test(string_for_check):
    for i in range(len(string_for_check)):
        string_for_check[i] = 2 * int(string_for_check[i]) - 1
    return abs(sum(string_for_check)) / math.sqrt(len(string_for_check)) <= 1.82138636


def sequence_identical_bits(string_for_check):
    string_lenght = len(string_for_check)
    frequency_of_units = string_for_check.count(1) / string_lenght
    Vn = 1
    for i in range(string_lenght - 1):
        if string_for_check[i] == string_for_check[i+1]:
            Vn += 0
        else:
            Vn += 1
    numerator = abs(Vn - 2 * frequency_of_units * string_lenght * (1 - frequency_of_units))
    denominator = 2 * math.sqrt(2 * string_lenght) * frequency_of_units * (1 - frequency_of_units)
    S = numerator / denominator
    return S <= 1.82138636


def read_file(reading_file):
    f = open(f"source/{reading_file}.txt", 'r')
    str_to_list = list(f.read())
    return str_to_list


def init():
    print("Первая лабораторная")
    while True:
        print("Введите размер файла:")
        file_size = input()
        generate_binary_file(int(file_size), "first_lab")
        result = read_file("first_lab")
        x: str = "Частотный тест пройден" if frequency_test(result) else "Последовательность не случайна"
        print(x)
        y: str = "Тест на последовательность одинаковых бит пройден" if sequence_identical_bits(result) else "Последовательность не случайна "
        print(y)
        print("'любая клавиша' - сгенерировать новый файл '0' - закончить")
        end = input()
        if end == '0':
            break
