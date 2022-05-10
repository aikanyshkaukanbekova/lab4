"""
Составьте программу, которая по номеру дня в году выводит число и месяц
в общепринятой форме (например, 33-й день года - 2 февраля).
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    NumDay = int(input('add number day'))
    if NumDay <= 31:
        print(NumDay, f'-й день года - ', NumDay, '.01', sep='')
    else:
        m = 0
        month = 0
        day = 0
        for month in range(1, 13):
            if month == 2:
                a = 28
            elif (month == 1 or month == 3 or month == 5 or month == 7 or
                  month == 8 or month == 10 or month == 12):
                a = 31
            else:
                a = 30
            m += a
            if NumDay - m <= 31:
                day = NumDay - m
                if NumDay > 31:
                    month += 1
                break

        if month < 10:
            print(NumDay, f'-й день года - ', day, '.0', month, sep='')
        else:
            print(NumDay, '-й день года - ', day, '.', month, sep='')
