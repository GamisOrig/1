print('*Калькулятор перевода из n-ричной в n-ричную*')
number = int(input('Введите число:\n'))
numSys1 = int(input('Введите систему счисления:\n'))

if 1 < numSys1 < 33:
    numSys2 = int(input('Введите желаемую систему счисления:\n'))

    if numSys2 == numSys1:
        print('Нечего переводить')

    elif 1 < numSys2 < 33:

        '''разложениe числа и нахождения маскимального'''
        decdNum = [int(i) for i in str(number)]

        # проверка на соответствие сс и числа
        if max(decdNum) >= numSys1:
            print('Некорректная система счисления для такого числа')

        else:
            # !!def из действительной сс в 10-сс:
            def _nto10(decdNum):
                print(decdNum, type(decdNum))
                rows = [int(i) for i in range(len(decdNum))]
                s = [decdNum[i] * numSys1 ** rows[i] for i in range(len(decdNum))]
                s = (sum(s))

                return s


            # !!def из 10-сс в 2-сс:
            def _10to2(number):
                s2 = []

                for i in range(1000, -1, -1):
                    n = 2 ** i

                    if number >= n:
                        number = number - n
                        s2.append(1)
                    else:
                        s2.append(0)

                s2 = int(''.join(map(str, s2)))

                return s2


            # !! def из 10-сс в желаемую сс:
            def _10ton(number):
                _d2 = []
                d = 0

                while number > 0:
                    d = number % numSys2
                    number = number // numSys2
                    _d2.append(d)
                print(_d2)
                _d2 = _d2[::-1]
                _d2 = int(''.join(map(str, _d2)))
                print(type(_d2))

                return _d2


            # !! def из действительной сс в желаемую сс:
            def _nton(number):
                _nto10(number)

                if numSys2 != 2:
                    return _10ton(_nto10(decdNum))
                else:
                    return _10to2(_nto10(decdNum))


            # !!из действительной сс в 10-сс:
            if numSys2 == 10:
                decdNum.reverse()
                print(_nto10(decdNum))

            # !!из 10-сс в 2-сс
            elif numSys1 == 10 and numSys2 == 2:
                print(_10to2(number))

            # !!из 10-сс в желаемую сс
            elif numSys1 == 10 and numSys2 != 10:
                print(_10ton(number))

            # !!из действительной сс в желаемую сс:
            elif numSys2 != 10 and numSys2 != 10:
                print(_nton(number))

    else:
        print('Некорректная желаемая система счисления')

else:
    print('Некорректная действительная система счисления')
