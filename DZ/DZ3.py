# a = 0
# b = 0
# n = 0
# while True:
#     print("Выберите операцию: ")
#     print('1' "(r) - выход из программы ")
#     print('2' "(+) - сложение ")
#     print('3' "(-) - вычетание ")
#     print('4' "(/) - деление ")
#     print('5' "(*) - умножение ")
#     print('6' "(%) - деление по модулю (остаток) ")
#     print('7' "(<) - минимальное из двух чисел ")
#     print('8' "(>) - максимальное из двух чисел ")
#     n = int(input("Введите цифру: "))
#     if 9 > n > 0:
#         break
# if 9 > n > 0 and n != 1:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
# if n == 1:
#     print("Выход из программы")
# if n == 2:
#     print(a + b)
# if n == 3:
#     print(a - b)
# if n == 4 or n != 0:
#     try:
#         if n == 4:
#             print(a / b)
#             # break
#     except ZeroDivisionError:
#         if n == 0:
#             print(a / b)
#         print("На ноль делить нельзя! ")
#         while True:
#             b = int(input("Введите повторно число делителя : "))
#             if b != 0:
#                 print(a / b)
#                 break
# if n == 5:
#     print(a * b)
# if n == 6:
#     print( a % b )
# if n == 7:
#     if a > b:
#         print(b)
#     elif a < b:
#         print(a)
# if n == 8:
#     if a > b:
#         print(a)
#     elif a < b:
#         print(b)
# print("Ок!")