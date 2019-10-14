# В римской системе счисления для обозначения чисел
# используются следующие символы:
#
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#
# Будем использовать вариант, в котором числа
# 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего:
# IV, IX, XL, XC, CD и CM, соответственно.
#
# Формат ввода:
# Строка, содержащая натуральное число 𝑛, 0 < n < 40000.
# Формат вывода:
# Строка, содержащая число, закодированное в римской системе счисления.

def get1(n):
    return 'M' * n

def get2(n):
    if n < 4:
        return 'C' * n 
    elif n == 4:
        return 'CD'
    elif 4 < n < 9:
        return 'D' + ('C' * (n - 5))
    elif n == 9:
        return 'CM'

def get3(n):
    if n < 4:
        return 'X' * n 
    elif n == 4:
        return 'XL'
    elif 4 < n < 9:
        return 'L' + ('X' * (n - 5))
    elif n == 9:
        return 'XC'

def get4(n):
    if n < 4:
        return 'I' * n 
    elif n == 4:
        return 'IV'
    elif 4 < n < 9:
        return 'V' + ('I' * (n - 5))
    elif n == 9:
        return 'IX'

def arabic_to_roman(inp):
	num = int(inp)
	ln = []
	lst = []

	ln = [num // 1000, num % 1000 // 100, num % 100 // 10, num % 10]
	lst = [get1(ln[0]), get2(ln[1]), get3(ln[2]), get4(ln[3])]
	return ''.join(lst)

inp = input()
print(arabic_to_roman(inp))
