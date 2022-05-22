# !!def из действительной сс в 10-сс:
def _nto10(decomposedNum, numSys1):
    rows = [int(i) for i in range(len(decomposedNum))]
    s = [decomposedNum[i] * numSys1 ** rows[i] for i in range(len(decomposedNum))]

    return sum(s)


# !! def из 10-сс в желаемую сс:
def _10ton(number, numSys2):
    _d2 = []
    d = 0
    _d2 = []
    while number > 0:
        d = number % numSys2
        number = number // numSys2
        _d2.insert(0, d)

    _d2 = int(''.join(map(str, _d2)))

    return _d2


# !! def из действительной сс в желаемую сс:
def _nton(decdNum, numSys1, numSys2):
    return _10ton(_nto10(decdNum, numSys1), numSys2)


def question(number, decdNum, numSys1, numSys2):
    if numSys1 == 10: return _10ton(decdNum, numSys2)
    elif numSys2 == 10: return _nto10(decdNum, numSys1)
    else: return _nton(decdNum, numSys1, numSys2)


def request():
    number = int(input('Введите число:\n'))
    numSys1 = int(input('Введите систему счисления:\n'))

    if 1 < numSys1 < 33:
        numSys2 = int(input('Введите желаемую систему счисления:\n'))

        if numSys2 == numSys1:
            print('Нечего переводить')

        elif 1 < numSys2 < 33:

            '''разложениe числа'''
            decdNum = [int(i) for i in reversed(str(number))]

            # проверка на соответствие сс и числа
            if max(decdNum) >= numSys1:
                print('Некорректная система счисления для такого числа')

            else:
                return question(number, decdNum, numSys1, numSys2)

        else:
            print('Некорректная желаемая система счисления')

    else:
        print('Некорректная действительная система счисления')

if __name__ == '__main__':
    print('*Калькулятор перевода из n-ричной в n-ричную*')
    print(request())
