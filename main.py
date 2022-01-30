import first, second, four, five, third
if __name__ == '__main__':
    while True:
        print("введите номер лабораторной работы:")
        a = input()
        if a == '1':
            first.init()
        elif a == '2':
            second.init()
        elif a == '3':
            third.init()
        elif a == '4':
            four.init()
        elif a == '5':
            five.init()