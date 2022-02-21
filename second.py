import time
import first
import math


def frequency_test(string_for_check):
    for i in range(len(string_for_check)):
        string_for_check[i] = 2 * int(string_for_check[i]) - 1
    return abs(sum(string_for_check)) / math.sqrt(len(string_for_check)) <= 1.82138636


def generic_symbol(x):
    temp = ((16807 * x) % 2147483647)-1
    return int(temp)


def init():
    print("Вторая лабораторная работа")
    print("введите длину последовательности")
    len_of_string = input()

    temp = int(time.time())
    result_string = ""
    for _ in range(int(len_of_string)):
        temp = generic_symbol(temp)
        res = (temp % 2)
        # print(res)
        result_string += str(res)

    check_list = list(result_string)
    x: str = "Частотный тест пройден" if frequency_test(check_list) else "Частотный тест не пройден"
    print(x)
    y: str = "Тест на последовательность одинаковых бит пройден" if first.sequence_identical_bits(
        check_list) else "Тест на последовательность одинаковых бит не пройден"
    print(y)

    file2 = open("source/second.txt", "w")
    file2.write(result_string)
    file2.close()