# !!def из действительной сс в 10-сс:
def _nto10(decomposedNum, numSys1):
    rows = [int(i) for i in range(len(decomposedNum))]
    s = [decomposedNum[i] * numSys1 ** rows[i] for i in range(len(decomposedNum))]

    return sum(s)


# !! def из 10-сс в желаемую сс:
def _10ton(number, numSys2):
    decdBySys = []
    while number > 0:
        buff = number % numSys2
        number //= numSys2
        decdBySys.insert(0, buff)

    newNum = int(''.join(map(str, decdBySys)))

    return newNum


# !! def из действительной сс в желаемую сс:
def _nton(decdNum, numSys1, numSys2):
    return _10ton(_nto10(decdNum, numSys1), numSys2)


def question(number, decdNum, numSys1, numSys2):
    if numSys1 == 10: return _10ton(number, numSys2)
    elif numSys2 == 10: return _nto10(decdNum, numSys1)
    else: return _nton(decdNum, numSys1, numSys2)


def crrctnes(numSys1, numSys2, decdNum):
    if 1 < numSys1 < 33:
        if numSys2 != numSys1:
            if 1 < numSys2 < 33:
                # проверка на соответствие сс и числа
                if max(decdNum) < numSys1:
                    return True
                else:
                    print('Некорректная система счисления для такого числа')
                    exit()
            else:
                print('Некорректная желаемая система счисления')
                exit()
        else:
            print('Нечего переводить')
            exit()
    else:
        print('Некорректная действительная система счисления')
        exit()


def request():
    number = int(input('Введите число:\n'))
    numSys1 = int(input('Введите систему счисления:\n'))
    numSys2 = int(input('Введите желаемую систему счисления:\n'))
    decdNum = [int(i) for i in reversed(str(number))]
    if crrctnes(numSys1, numSys2, decdNum):
        return question(number, decdNum, numSys1, numSys2)


if __name__ == '__main__':
    print('*Калькулятор перевода из n-ричной в n-ричную*')
    print(request())
