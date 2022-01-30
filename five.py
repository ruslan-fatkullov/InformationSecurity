import math
import random


class PrivateKey(object):
    def __init__(self, p=None, g=None, x=None):
        self.p = p
        self.g = g
        self.x = x


class PublicKey(object):
    def __init__(self, p=None, g=None, h=None):
        self.p = p
        self.g = g
        self.h = h


# проверка числа на простоту тестом Лемана
def lehman_test(p):
    count = 7
    a = random.randint(2, p - 1)
    e = int((p - 1) / 2)
    while count > 0:
        result = (a ** e) % p
        if (result % p) == 1 or (result % p) == (p - 1):
            a = random.randint(2, p - 1)
            count = count - 1
        else:
            return False
    return True


# генерирование простого числа в диапазоне 2^bits_start - 2^bits_end
def generate_prime(bits_start, bits_end):
    p = random.randint(2 ** bits_start, 2 ** bits_end)
    print('подбор простого числа...')
    while 1:
        if lehman_test(p):
            return p
        else:
            p = random.randint(2 ** bits_start, 2 ** bits_end)


# генерация открытого и закрытого ключей
def generate_keys():
    p = generate_prime(10, 16)
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 1)
    h = (g ** x) % p
    publicKey = PublicKey(p, g, h)
    privateKey = PrivateKey(p, g, x)
    return {'privateKey': privateKey, 'publicKey': publicKey}


# генерация взаимно простого относительно p числа
def mutually_prime_numbers(p):
    while (1):
        count = 0
        a = random.randint(2, p - 1)
        for i in range(1, a + 1):
            if a % i == 0 and p % i == 0:
                count += 1
        if count == 1:
            return a


# возведение в степень и взятие остатка от деления
def modexp(base, exp, modulus):
    return pow(base, exp, modulus)


# кодирование одного символа
def encode(key, message):
    k1 = mutually_prime_numbers(key.p - 1)
    a = modexp(key.g, k1, key.p)
    b = (message * modexp(key.h, k1, key.p)) % key.p
    return a, b


# декодирование одного символа
def decode(key, a, b):
    s = modexp(a, key.x, key.p)
    decrypt_symbol = (b * modexp(s, key.p - 2, key.p)) % key.p
    return decrypt_symbol


# кодирование строки
def encrypt(string, publicKey):
    str_list = list(string)
    pairs = []
    for i in str_list:
        a, b = encode(publicKey, ord(i))
        pairs.append([a, b])
    result = ""
    for pair in pairs:
        tmp = str(pair[0]) + " " + str(pair[1]) + " "
        result += tmp
    return result


# декодирование строки
def decrypt(string, key):
    str_list = string.split(" ")
    str_list.pop()
    result = ""
    for i in range(0, len(str_list), 2):
        decrypt = decode(key, int(str_list[i]), int(str_list[i+1]))
        result += chr(decrypt)
    return result


# запись в файл
def write_to_file(text, filename):
    file = open('source/{0}.txt'.format(filename), "w")
    file.write(text)
    file.close()


def init():
    keys = generate_keys()
    privateKey = keys['privateKey']
    publicKey = keys['publicKey']

    print("открытый ключ")
    print(publicKey.p)
    print(publicKey.g)
    print(publicKey.h)
    print("закрытый ключ")
    print(privateKey.p)
    print(privateKey.g)
    print(privateKey.x)
    file = open('source/five_lab_input.txt', 'r')
    input_text = file.read()
    encrypted = encrypt(input_text, publicKey)
    write_to_file(encrypted, "five_lab_encrypted")
    print("Шифрованный текст:")
    print(encrypted)

    enc_file = open('source/five_lab_encrypted.txt', 'r')
    encrypted_text = enc_file.read()
    decrypted = decrypt(encrypted_text, privateKey)

    print("Дешифрованный текст:")
    print(decrypted)
    write_to_file(decrypted, "five_lab_decrypted")