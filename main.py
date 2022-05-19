print('*Калькулятор перевода из n-ричной в n-ричную*')
number = int(input('Введите число:'))
ss1 = int(input('Введите систему счисления:'))

if 1 < ss1 < 33:
    ss2 = int(input('Введите желаемую систему счисления:'))
    if ss2 == ss1:
        print('Нечего переводить')
    elif 1 < ss2 < 33:

        '''def разложения числа и нахождения маскимального'''


        def _rc(number):
            ns1 = []

            while number > 0:
                ns1.append(number % 10)
                number = number // 10

            ns1 = ns1[::-1]
            m = max(ns1)
            return m


        # проверка на соответствие сс и числа
        if _rc(number) >= ss1:
            print('Некорректная система счисления для такого числа')
        else:
            # !!def из действительной сс в 10-сс:
            def _nto10(number):
                ns = []
                lc = len(str(number))
                _lc = []
                s = []

                while number > 0:
                    ns.append(number % 10)
                    number = number // 10

                ns = ns[::-1]

                while lc > 0:
                    lc = lc - 1
                    _lc.append(lc)

                for i in range(0, len(ns)):
                    s.append(ns[i] * ss1 ** _lc[i])
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
                    d = number % ss2
                    number = number // ss2
                    _d2.append(d)

                _d2 = _d2[::-1]
                _d2 = int(''.join(map(str, _d2)))
                print(type(_d2))

                return _d2


            # !! def из действительной сс в желаемую сс:
            def _nton(number):
                _nto10(number)

                if ss2 != 2:
                    return _10ton(_nto10(number))
                else:
                    return _10to2(_nto10(number))


            # !!из действительной сс в 10-сс:
            if ss2 == 10:
                print(_nto10(number))

            # !!из 10-сс в 2-сс
            elif ss1 == 10 and ss2 == 2:
                print(_10to2(number))

            # !!из 10-сс в желаемую сс
            elif ss1 == 10 and ss2 != 10:
                print(_10ton(number))

            # !!из действительной сс в желаемую сс:
            elif ss1 != 10 and ss2 != 10:
                print(_nton(number))

    else:
        print('Некорректная желаемая система счисления')

else:
    print('Некорректная действительная система счисления')
