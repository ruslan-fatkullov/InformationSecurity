import time
import first


def generic_symbol(x):
    x = ((16807 * x) % 2147483647)-1
    return int(x)


def init():
    print("Вторая лабораторная работа")
    print("введите длину последовательности")
    len_of_string = input()
    result_list_of_numbers = list()
    temp = int(time.time())
    for _ in range(int(len_of_string)):
        temp = generic_symbol(temp)
        result_list_of_numbers.append(format(temp, 'b'))

    result_string = ""
    for i in result_list_of_numbers:
        result_string += i

    file2 = open("source/second.txt", "w")
    file2.write(result_string)
    file2.close()

    check_list = list(result_string)
    x: str = "Частотный тест пройден" if first.frequency_test(check_list) else "Частотный тест не пройден"
    print(x)
    y: str = "Тест на последовательность одинаковых бит пройден" if first.sequence_identical_bits(
        check_list) else "Тест на последовательность одинаковых бит не пройден"
    print(y)