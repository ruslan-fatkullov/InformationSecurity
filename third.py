import hashlib


def xor_crypt_string(data, key, encode=False, decode=False):
    from itertools import cycle

    if decode:
        data = data.decode("utf-8")

    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))

    if encode:
        return xored.encode()
    return xored


def init():
    print("Лабораторная работа №3")
    file = open('source/third_lab_input.txt', 'r')
    print("Введит текстовый ключ:")
    key = input()
    string = file.read()

    print("Кодированный текст:")
    encoding = xor_crypt_string(string, key, encode=True)
    file = open('source/third_lab_coded.txt', 'w')
    file.write(encoding.decode("windows-1251"))
    file.close()
    print(encoding)

    print("Декодированный текст:")
    decoding = xor_crypt_string(encoding, key, decode=True)
    my_file = open("source/third_lab_decoded.txt", "w")
    my_file.write(decoding)
    my_file.close()
    print(decoding)

    print("Хешированный ключ хеш-функцией MD-5:")
    hash_key = hashlib.md5(key.encode()).hexdigest()
    print(hash_key)
