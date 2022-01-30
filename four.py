import numpy as np
import hashlib

# функция кодирования одного блока
# в список добавляются численные значения каждого символа в блоке
# переданная ключ-матрица умножается на этот список и возвращается список закодированных символов
def encode(word, matrix):
    alpha_list = [ord(a) for a in word]
    encoded = matrix.dot(alpha_list)
    return encoded


# функция декодирования одного блока
# умножаем обратную матрицу на закодированный блок
# округляем дробные числа в сторону ближайшего целого
# возвращается список из символьных представлений декодированных чисел
def decode(coded_block, inverse_matrix):
    decode = inverse_matrix.dot(coded_block)
    decode_int = list()
    for g in decode:
        decode_int.append(round(g))
    char_lst = list()
    for g in decode_int:
        char_lst.append(chr(g))
    return char_lst


# запись в файл
def write_to_file(text, filename):
    file = open('source/{0}.txt'.format(filename), "w")
    file.write(text)
    file.close()


def init():
    print("Лабораторная 4")

    file = open('source/four_lab_input.txt', 'r')
    input_text = file.read()
    input_text_list = list()

    # дополнение текста пробелами до кратного 7
    if len(input_text) % 7:
        input_text += " " * (7 - len(input_text) % 7)

    # разбиение на слова по 7 байт
    [input_text_list.append(input_text[i:i + 7]) for i in range(0, len(input_text), 7)]

    # с помощью генератора случайных чисел задается матрица 7х7
    key_matrix = np.random.randint(0, 10, (7, 7))
    print("Матрица с рандомными числами:")
    print(key_matrix)

    # кодирование
    result_string = ""
    for word in input_text_list:
        # кодирование одного блока
        encoded_block = encode(word, key_matrix)
        for i in encoded_block:
            result_string += str(i) + " "
    print("Исходная строка:")
    print(input_text)
    print()
    print("Закодированная строка:")
    print(result_string)
    write_to_file(result_string, "four_lab_encoded")

    # декодирование
    encoded_file = open("source/four_lab_encoded.txt", "r")
    encoded_string = encoded_file.read()
    encoded_list = encoded_string.split(" ")
    encoded_list.pop()
    list_of_blocks = list()
    [list_of_blocks.append(encoded_list[i:i + 7]) for i in range(0, len(encoded_list), 7)]
    decoded_string = ""
    # находим обратную матрицу
    inverse_matrix = np.linalg.inv(key_matrix)
    for item in list_of_blocks:
        int_item = [int(i) for i in item]
        decoded_block = decode(int_item, inverse_matrix)
        for i in decoded_block:
            decoded_string += str(i)
    write_to_file(decoded_string, "four_lab_decoded")
    print()
    print("Декодированная строка:")
    print(decoded_string)

    f = list(key_matrix)
    key_matrix_str = ""
    for i in f:
        tmp = list(i)
        for j in tmp:
            key_matrix_str += str(j)
    hash_key = hashlib.md5(key_matrix_str.encode()).hexdigest()
    print("Хешированная ключ_матрица:")
    print(hash_key)