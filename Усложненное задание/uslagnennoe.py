#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-

импорт математики
импорт sys


ЭЙЛЕР = 0,5772156649015328606
EPS = 1e-10

если __name__ == '__main__':
    x = float(input("x = "))
    если x == 0:
        print("Ошибка", file=sys.stderr)
        выход(1)
    a = -x ** 2 / 4
    S, n = a, 1
    в то время как math.fabs(a)> EPS:
        a *= (-1 * x ** 2 * 2 * n) / (2 * (n + 1)) ** 2
        S += a
        n += 1
    print(f"Ci({x}) = {EULER + math.log(math.fabs(x)) + S}")