#!/usr/bin/env python3

# Ходы коня
# На шахматной доске 8×8 стоит конь.
# Напишите программу, которая отмечает положение коня на доске и все клетки.
# которые бьет конь.
# Клетку, где стоит конь, отметьте английской буквой N,
# клетки, которые бьет конь, отметьте символами *,
# остальные клетки заполните точками.
# На вход программе подаются координаты коня на шахматной доске
# в шахматной нотации. Например: b6, d4, e5


y0, x0 = list(input())
x = 8 - int(x0)
y = ord(y0) - ord('a')

for i in range(8):
    for j in range(8):
        if i == x and j == y:
            print('N', end=' ')
        elif (x-i)**2 + (y-j)**2 == 5:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
