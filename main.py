# name = "Alex"
# age = 24
# print("Hello " + name + ". I am " + str(age))
#
# print(type(name))
# print(type(age))
# print(id(name))
# print(id(age))

# Функция преобразования типов
# int() - числовой тип
# str() - строковый тип

# num1 = "2"
# num2 = 3
# # res = int(num1) + num2
# res = num1 + str(num2)
# print(res)
# print(type(res))

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)

# cnt = 10
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = int(input("Введите первую сторону треугольника: "))
# b = int(input("Введите вторую сторону треугольника: "))
# c = int(input("Введите третью сторону треугольника: "))
# if a == b == с:
#     print("Равностороний")
# elif a == b or b == c or c == a:
#     print("Равнобедренный")
# else:
#     print("Разностороний")

# day = int(input("Введите день недели(цифрой): "))
# if 1<= day <=5: #(day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Ошибка")

# a=int(input("Введите номер месяца: "))
# if 1<= a <= 2 or 11<= a <=12:
#     print("Зима")
# elif 3<= a <=6:
#     print("Весна")
# elif 7 <= a <= 8:
#     print("Лето")
# else:
#     print("Осень")

# ///////////////////////////////////////
# ОБРАБОТКА ИСКЛЮЧЕНИЙ В ПИТОНЕ
# a = input("Введите первое значение: ")
# b = input("Введите второе значение: ")
# try:
#     a=int(a)
#     b=int(b)
# except ValueError:
#     a=str(a)
#     b=str(b)
# finally:
#     print(a+b)

# while условие:
#     блок инструкций

# иттерация -повторение,один шаг цикла

# i = 1
# while i > 0:
#     print("i =", i)
#     i += 1

# i = 1
# while i <= 20:
#     if i % 2:
#         print(i, end=" ")
#     i += 1

# i = 0
# while i <= 1000:
#     print(i, end=" ")
#     i *= 10


# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Введите число начала диапозона: "))
# m = int(input("Введите число конца диапозона: "))
# res = 0
#  while n <= m:
#      if n % 2:
#          res +=n
#          print(n, end=" ")
#      n += 1
# print("Сумма целых нечетных чисел: ", res)


# a = [7, 9, 2, 1, 17, 25]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# срез
# список [start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s [1:4])
# print(s [2:])
# print(s [:2])
# print(s [::-1])
# print(s [5:0:-1])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[0:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3]= [0, 0, 0, 0]
# print(s)
# s[2] = 20
# print(s)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2

# print(int(3.8))
# print(round(3.894, 2))

# a = "5.2"
# b = 10
# c = float(a) + b
# print(c)
# print(type(c))

# name = "Victor"
# age = 28
# print("My name is ", name, 'my ', age, ' age', sep="")
# print("My name is " + name + 'my ' + str(age) + ' age.',end="\n\n")
# print("Я уже Python")

# num = int(input("Введите число:"))
# power = int(input("Введите степень:"))
# res = num ** power
# print("Число:", num, "в степени", power, "равно:", res)


# print(bool("Python"))
# print(bool(""))
# print(bool(0)) # False
# print(bool(-25))
# print(bool(15))

# print(7 == 7)
# print(7 + 2 == 7)
# print(7 + 2 != 7)
# print(8 > 5)
# print(8 < 5)

# print(2 < 4 < 9)


# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print (5 - 3 == 2 and 1 + 3 == 4) #True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4) #False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4) #False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4) #False (False:False)
# И в правой и в левой части должна быть истина (and - оператор сравнение "и")

# print (5 - 3 == 2 or 1 + 3 == 4) #True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4) #True (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4) #True (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4) #False (False:False)
# В правой или в левой части должна быть истина (or- оператор сравнения "или")
#
# print(not 9 - 5)
# print(not 5 - 5)
# not - оператор сравнения который меняет на противоположное


# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     pass
#     print("Доступ запрещен")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# a = int(input("Введите первую сторону треугольника: "))
# b = int(input("Введите вторую сторону треугольника: "))
# c = int(input("Введите третью сторону треугольника: "))
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or c == a:
#     print("Треугольник равнобедренный: ")
# else:
#     print("Треугольник разносторонний: ")

# day = int(input("Введите день недели (цифрой): "))
# # if (day >= 1) and (day <= 5):
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует!")

# x = int(input("Введите номер месяца от 1 до 12: "))
# if 1<= x <= 2:
#     print("Зима")
#     if x == 1:
#         print("Январь")
#     if x == 2:
#         print("Февраль")
# elif 3<= x <= 5:
#     print("Весна")
#     if x == 3:
#         print("Март")
#     if x == 4:
#         print("Апрель")
#     if x == 5:
#         print("Май")
# elif 6<= x <= 8:
#     print("Лето")
#     if x == 6:
#         print("Июнь")
#     if x == 7:
#         print("Июль")
#     if x == 8:
#         print("Август")
# elif 9<= x <= 11:
#     print("Осень")
#     if x == 9:
#         print("Сентябрь")
#     if x == 10:
#         print("Октябрь")
#     if x == 11:
#         print("Ноябрь")
# elif x == 12:
#     print("Зима")
#     print("Декабрь")
# else:
#     print("Такого месяца не существует! ")

# x = int(input("Введите количество ворон от 0 до 9: "))
# if 0 <= x <= 9:
#     if x == 1:
#         print("На ветке", x, "ворона")
#     if 2 <= x <= 4:
#         print("На ветке", x, "вороны")
#     if 5 <= x <= 9 or x==0:
#         print("На ветке", x, "ворон")
# else:
#     print("Ошибка ввода данных! ")

# n = int(input("Введите количество копеек от 0 до 99: "))
# if 1 <= n <= 99:
#     if 11 <= n <= 14:
#         print(n, "копеек")
#     else:
#         x = n % 10
#         if x == 1:
#             print(n, "копейка")
#         if 2 <= x <= 4:
#             print(n, "копейки")
#         if 5 <= x <= 9 or x == 0:
#             print(n, "копеек")
# else:
#     print("Ошибка ввода данных!")

# a = 5
# b = 0
# print( a/b )

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("ОК")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки!")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль!")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError,ZeroDivisionError):
#     print("Введены не корректные данные")
# else:
#     print("Все нормально вы ввели корректные числа", n, "и", m)
# finally:
#     print("Конец программы")

# x = input("Введите первое число: ")
# y = input("Введите второе число: ")
# try:
#     x = int(x)
#     y = int(y)
# except ValueError:
#     x = str(x)
#     y = str(y)
# finally:
#     print(x + y)

# while условие:
#     блок инструкций

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1 #или i = i + 1

# i = 10
# while i > 0 :
#     print("i =", i)
#     i -= 1 #или i = i - 1

# i = 2
# while i <= 20:
#     print("i = ", i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# n = int(input("Введите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Введите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# n = int(input("Введите начало диапозона: "))
# m = int(input("Введите конец диапозона: "))
# res = 0
# while n <= m:
#     if n % 2:
#         res += n
#         print(n, end=" ")
#     n += 1
# print("Сумма целых нечетных чисел:", res)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# n = input("Введите четное число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Не правильный ввод данных!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное!")
# else:
#     print("Нечетное!")

# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i >= 7:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i, end=",")
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное целое число: "))
#     if not n < 0:
#         break
#
# print(n)

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


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

# n = int(input("Введите количество символов: "))
# sim = input("Введите тип символа: ")
# orient = input("0 - горизонтальная\n1 - вертикальная\nВведите ориентацию символов: ")
# i = 0
# while i < n:
#     if orient == "0":
#         print(sim, end=" ")
#     elif orient == "1":
#         print(sim)
#     else:
#         print("Такой ориентации не предусмотренно!")
#         break
#     i += 1

# number = int(input("Введите количество чисел последовательности: "))
# i = 1
# n = float(input("Введите число: "))
# summa = n
# minim = n
# maxim = n
# while i < number:
#     n = float(input("Введите число: "))
#     summa += n
#     if maxim < n:
#         maxim = n
#     if minim > n:
#         minim = n
#     i += 1
# print("Cреднее арифметическое равно: ", summa / number)
# print("Минимальное значение равно: ", minim)
# print("Минимальное значение равно: ", maxim)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for i in 5, 6, 7, 8, 9:
#     print(i)


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")


# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")
#

# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = [i for i in range(6) if i % 2 == 0]
# print(n)

# n = [i * 2 for i in "Hello"]
# print(n)


# Тип данных - список(позволяет поддерживать разные типы данных)
# n = [5, 6, [7, 8, 9], "Hello", 5.6, True]
# # print(n)
# # print(type(n))
# # print(n[2][2])
# # print(n[3][1])
# n[1] = 256
# n[0] += 100
# print(n)
# print(len(n))

# s = [1, 2, 3]
# print(s)
#
# b = list('Hello')
# print(b)

# s = [1, 2, 3]
# print([5] * 6)

# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(id(n))
# print(n2)
# print(id(n2))
# if n is n2:
#     print('Списки равны')
# else:
#     print('Списки разные')

# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# n = 5
# for i in range(1, n + 1):
#     print([i ** 2], end=" ")

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)

# print([int(input("->")) for i in range(int(input("n = ")))])

# n = [2, 4, 6, 8]
# for i in range(len(n)):
#     print(n[i], end=" ")
# print()
# for elem in n:
#     print(elem, end=" ")


# a = [int(input("->")) for i in range(int(input("n = ")))]
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print("Сумма отрицательных элементов: ", b)

# a = [int(input("->")) for i in range(int(input("n = ")))]
# b = 0
# c = 0
# for i in range(len(a)):
#     if a[i] % 2:
#         b += a[i]
#     elif a[i] % 2 == 0:
#         c += 1
# print("Сумма нечетных элементов: ", b)
# print("Количество четных элементов: ", c)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     elif n[i] % 2:
#         s += n[i]
# print('Cумма нечетных чисел: ', s)
# print('Количество четных чисел: ', k)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     elif i % 2:
#         s += i
# print('Cумма нечетных чисел: ', s)
# print('Количество четных чисел: ', k)

# a = [int(input("->")) for i in range(int(input("Введите количество элементов списка: ")))]
# sr_a = k = 0
#
# for i in a:
#     if i > 0:
#         sr_a += i
#         k += 1
#         sr_a = sr_a / k
# print(sr_a)

# a = [7, 9, 2, 1, 17]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# Срез- это получение какой-то части списка,которая в свою очередь тоже будет являться списком
# список[star:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[::-1])  #разворачивает список
# print(s[5:1:-1])  # разворачивает с заданным диапазоном

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1:6:2])
# print(s[:1])
# print(s[-1])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:3] = [20]# если диапазон то скобки
# s[2] = 20 # если одно число то можно вот так
# s[2] = [20] # вложенный список
# s[12:]= [9, 18, 28, 38, 48]
# print(s)
# print(s[10])

# Методы списков
# s = [5, 9, 3, 7, 1, 8]
# s.append(99) # добавляет элемент в конец списка
# s.extend([91, 23]) # добавляет cписок в конец основного списка (обязательно [])
# print(s)
# s.extend('add') # добавляет строку по буквам(каждая буква как отдельный элемент)
# print(s)
# # если мы хотим указать не в конец списка
# s.insert(1,100) #первым параметром(1) это индекс куда вставить,второй параметр (100) это число которое вставляем!НЕ ПЕРЕЗАПИСЫВАЕТ
# print(s)

# Программа которая будет просить пользователя заданное кол-во раз
# просить пользователя ввести число и каждый раз это число добавлять
# в список, а потом выведет этот список с выводом всех существующих элементов

# s = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("->"))
#     s.append(x)
# print(s)

# s = []
# n = int(input("Введите количество элементов списка: "))
# for i in range(n):
#     x = int(input("Введите число кратное 3:"))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка.")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0

# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)
# # for i in range(len(a)):
# #     c.append(a[i])
# #     c.append(b[i])
# # print(c)

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# # # s.remove(9) # удаляет первый искомый элемент из списка по значению
# # # print(s)
# # last = s.pop() # без параметров - удаляет последний элемент из списка
# # last1 = s.pop(0)
# # print(last)
# # print(last1) # c указанным параметром удаляет значение из списка по индексу,и добавляет в переменную
# # print(s)
# # s.clear() # удаляет из списка все элементы
# # print(s)
# del s[:] # очищает список через срез
# del s[2:4] # удаляет диапозон элементов по заданному индексу через срез
# print(s)

# a = [int(input("->")) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)
# b = int(input("Введите индекс:"))
# a.pop(b)
# print(a)

# s = [5, 9, 3, 7, 1, 8, 9, 9, 9, 9, 3]
# num = s.count(9) # count выводит количество значений в данном случае сколько (9)
# print(num)
# print(s)
# ind = s.index(7)  # index нахолит индекс по значению элемента
# ind1 = s.index(3,4) # index находит значение (3) начиная с 4-го индекса
# print(ind)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)

# s = [5, 9, 3, 7, 1, 8, 9, 9, 9, 9, 3]
# print(s)
# s.reverse() # разворачивает список
# print(s)
# Сортировка списка
# s = [5, 9, 3, 7, 1, 8, 9, 9, 9, 9, 3]
# print(s)
# # s.sort() # по умолчанию сортирует по возрастанию
# # print(s)
# # a = sorted(s) # сортирует в переменную не изменяя основной список
# # print(a)
# # print(s)
# # s.sort(reverse=True) # по умолчанию сортирует по убыванию, изменяет список
# # s.sort(reverse=False) # по умолчанию сортирует по возрастанию, изменяет список
# # print(s)
# a = sorted(s, reverse=True)  #сортирует в порядке убывания, не изменяя список основной

# s2 = ["Виталий", "Сергей", "Александр","Анна"]
# s2.sort(key=len) # сортировка по количеству букв в слове(возростание)
# s2.sort() # по алфавиту
# s2.sort(key=len, reverse=True) # тоже по алфавиту
# print(s2)

# import random
#
# print(random.random())
# print(random.randint(1, 10))
# print(random.randrange(0, 20, 2))

# from random import randint, randrange # импорт определенных методов
# print(randint(1, 10))
# print(randrange(0, 20, 2))

# from random import * # * - импортирует все методы
# print(randint(1, 10))
# print(randrange(0, 20, 2))

# print(r.randint(1, 10))  # должен обязательно иметь два значение (от) и (до)
# print(r.randrange(10, 100, 2))  # может иметь три значения(от,до,шаг)
#
# # кроме генерации случайных чисел есть элементы которые мы можем импортировать из самого модуля random
#
# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))  # выбирает случайный элемент из списка
#
# s = [55, 65, 3, 2, 32]
# print(r.choice(s))  # выбирает один случайный элемент из списка
#
# s = [32, 21, 44, 32, 54, 23, 21, 54, 76, 43, 32, 222, 21]
# print(r.choices(s, k=3))  # выбирает несколько случайных элементов(к = 3 указывает кол-во)
#
# r.shuffle(s)  # перемешивает случайным образом элементы в списке
# print(s)
#
# print(r.uniform(10.5, 25.5))  # случайное вещественное число с заданным диапозоном от 10.5 до 25.5
# print(round(r.uniform(10.5, 25.5), 2))  # round округляет,а , 2)) - указывает на сколько знаков после запятой округлять

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# Функция агрегирования - это набор готовых функций которые за нас выполняют какие-то действия

# lst = [5, 3, 2, 4, 1]
# print(len(lst)) # показывает количество элементво в списке
# print(max(lst)) # максимальное значение из списка
# print(min(lst)) # минимальное значение из списка
# print(sum(lst)) # сумма элементов списка

# mas = [r.randint(0, 100)for i in range(10)]
# print(mas)
# print(max(mas))
# mas.sort(reverse=True)
# print(mas)

# mas = [r.randint(0, 100)for i in range(10)]
# print(mas)
# m = max(mas)
# print('Max:', m)
# mas.remove(m)
# mas.insert(0, m)
# print(mas)

# mas = [r.randint(-20, 20)for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# mas = [r.randint(1, 100)for i in range(10)]
# print(mas)
# minim = min(mas)
# ind = mas.index(minim)
# print(minim)
# print(ind)
# del mas[:ind]
# print(mas)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# if len(lst) == 0:
#     print("Список пуст")
# if not lst:
#     print("Список пуст")

# n1 = int(input("Количество элементов 1-го списка: "))
# n2 = int(input("Количество элементов 2-го списка: "))
# a = [r.randint(0, 10)for i in range(n1)]
# b = [r.randint(0, 10)for j in range(n2)]
# print("a =", a)
# print("b =", b)
# c = a + b
# print("c =", c)
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# for i in b:
#     if i not in c:
#         c.append(i)
# print("Элементы обоих списков без повторений", c)
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для двух списков", c)
# c = [min(a), min(b), max(a), max(b)]
# print("Минимальные и максимальные числа в списках: ", c)

# n = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#      ]
# print(n)
# # print(len(n))
# # print(m[1][2])
# for row in range(len(n)):
#     for col in range(len(n[row])):
#         print(n[row][col], end="\t\t")
#     print()
# print()
# for row in n:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)

# num1 = math.sqrt(36)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# print(num1)
# print(num2)
# print(num3)
#
# print(dir(math))
# print(math.pi)

# rd = int(input("Введите радиус окуржности: "))
# print("Длина окружности: ", round(2 * math.pi * rd, 2))

# seconds = time.time()
# print("Секунды с начала эпохи: ", seconds)
# locale_time = time.ctime()
# print("Местное время: ", locale_time)
# res = time.localtime()
# print("Localtime:", res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep='')
# print(time.strftime("Today is %B %d, %Y."))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 5
# print("Programm started...")
# time.sleep(pause)
# print(pause, "seconds.")

# text = input('Название напоминания: ')
# locale_time = float(input('Через сколько минут: '))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, 'seconds')

# start = time.monotonic()
# time.sleep(5)
# res = time.monotonic() - start
# print(res, 'seconds')

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime('Сегодня: %B %d, %Y.'))

# Функция - это подпрограмма которую можно вызвать в любой части кода и вызывать можно любое кол-во раз


# def hello(name):  # агрументы
#     print('Hello', name)
#
#
# hello("Irina")  # параметры
# hello("Igor")

# def get_sum(x, y):
#     print(x + y)
#
#
# a = 2
# b = 5
# get_sum(a, b)
# n = 6
# m = 4
# get_sum(n, m)
# get_sum("abc", "def")
# get_sum(6.5, 3.3)

# def symbol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end="")
#         else:
#             print(c, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     print(a + b)
#     return a+b
#
#
# res = get_sum(1, 8)
# print(res)
# print(get_sum(2, 5))

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 15))

# x = int(input("Введите первое число: "))
# y = int(input("Введите второе число: "))


# def sum_raz(a, b):
#     if a > b:
#         return a - b
#     elif a < b:
#         return a + b
#
#
# print(sum_raz(x, y))

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#
#
# fib(15)


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(10, 15))

# Программа проверка пороля
# Проверяет есть ли в коде заглавные,маленькие буквы и цифры
#
# def check_password(password):
#     has_upper = False # большие буквы
#     has_lower = False # маленькие буквы
#     has_num = False # цифры
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Не надежный пароль")


# def get_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(4, 3, 1, 6))
# print(get_sum(3, 1, 6))
# print(get_sum(3, 6))
# print(get_sum(3, 1, 6))
# print(get_sum(3, 1, c=1))


# def symbol(x=20, y='-'):
#     for i in range(x):
#         print(y, end='')
#     print()
#
#
# symbol(10, '+')
# symbol(5, '*')
# symbol(15, '#')
# symbol(15)
# symbol()

# def digits_sum(n, event=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if event and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not event and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных чисел: ")
# print(digits_sum(9874023, event=False))
# print(digits_sum(38271, event=False))
# print(digits_sum(123456789, event=False))

# def display_info(name, age):
#     print("Name: ", name, "\nAge", age)
#
#
# display_info("Ira", 20)
# display_info(age=20, name="Ira")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))

# s = "Hello "
# print(id(s))
# s += "World"
# print(s)
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))

# a = 'Hello'
# b = 'Hello'
# print(a == b)
# print(a is b)
#
# a = 5
# b = 5
# print(a == b)
# print(a is b)

# def add_numbers(n):
#     print('Внутри функции: ', n, '=', id(n))
#     n += 1
#     print("После изменения: ", n, '=', id(n))
#     return n
#
# x = 1
# print(x, "=", id(x))
# x = add_numbers(x)
# print(x, "=", id(x))


# def square(x, y):
#     if p == 1:
#         s = x * y
#         print(s)
#     elif p == 2:
#         s = x / 2 * y
#         print(s)
#     elif p == 3:
#         s = x + y
#         print(s)
#     else:
#         print("Неправильный ввод данных выбора фигур!")
#
#
# p = int(input("Выберите площадь фигуры: 1-прямоугольник, 2-треугольник, 3-круг : "))
# n = int(input("Основание,n: "))
# h = int(input("Высота,h: "))
# square(n, h)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = tuple((1, 5, 6, 7, 8))
# print(a)
# print(type(a))
# b = tuple()
# print(type(b))

# q = 1, 2, 3, "w"
# t = (1,)
# print(type(t))
# print(type(q))
# t1 = tuple("hello")
# print(t1)
# print(t1[1:3])
# t1[1] = 'i'

# s1 = tuple(float(input("->")) for i in range(5))
# print(s1)

# s = input("->")
# print(tuple(s))

# mas = [r.randint(0, 100) for i in range(10)]
# tpl = tuple(mas)
# print(tpl)

# mas = tuple[r.randint(0, 100) for i in range(10)]
# print(mas)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count("l")) # количество элементов l
# # print(t3.index("l")) # индекс элемента l
# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
#
# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user[1])
# print(user[0])

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# print(type(tpl))
# print(list(tpl))

# countries =(
#     ("Германия", 20.2, (('Берлин', 3.326),('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2),('Марсель',1.6)))
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана", country_name,"население = ", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород", city_name, "население = ", city_population)


# Множества (set) - это неупорядоченная коллекция, которая хранит только уникальные значения
# {}
# set()

# s = {"s", "a", 4, 7, 8, 9, 4, 2, 4, 2, 4}
# print(type(s))
# print(len(s))
# print(s)

# s = set('hello')
# print(s)

# c = [1, 2, 3, 4, 5, 3, 6]
# s = set(c)
# print(s)
# c = list(s)
# print(c)

# numbers = [1, 2, 2, 2, 4, 5, 6, 3, 3, 2, 5]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# def to_set(el):
#     # st = set(el) # perviy variant
#     # return st, len(st)
#
#     return set(el), len(set(el))  # vtoroi variant
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {"red", 'green', 'blue'}
# # print('green' in t)
# for i in t:
#     print(i)

# {i for i in последовательность}
# {i for i in последовательность if(условие)}
# {i (True) if условие else i(False)for i in последовательность}
# {i (True) if условие else i(False)for i in последовательность if условие}

# e = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in r if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in e if i[1] == 'c'}
# print(a)

# a = {"Tom", "Bob", "Alice"}
# a.add("Anna")
# print(a)
# # b = 'Tom1'
# # if b in a:
# #     a.remove(b)
# # a.discard('Tom')
# # a.pop()
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # print(c)
# c = a - b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print('Unic elems count:', len(s))
# print("Min elem: ", min(s))
# print("Max elem: ", max(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# paint = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
#
# one = paint ^ music
# print(one)
#
# two = set(paint) & set(music)
# print(two)
#
# paint = paint - two
# print(paint)


# # Тип frozenset- замороженное множество
# a = frozenset([1, 2, 3, 4, 5])
# print(a)
# s = frozenset({"hello", 'world'})
# print(s)

# Словарь dict()

# lst = list["one", 'two', 'three']
# print(lst)
# print(lst[0])
# d = {'a': "one", 'b': 'two', 'c': "three"}
# print(d["b"])
# print(d)

# d = {'one': 1, 2: "two"}
# print(d['one'])
# print(type(d))

# d = dict(short='dict', long='dictionary')
# print(d)
# print(type(d))

# user = [['p.alexvz98@mail.ru', 'Alex']]
# print(user)
# d_user = dict(user)
# print(d_user)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[2])
# d[2] = 15
# d[9] = 4**2
# print(type(d))
# print(d)

# d = {0: 'text', 'one': 45, (1, 2, 3): 'Кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# # print(d[True])
# # print(d[42][1])
# #
# # print('one' in d)
# # print('two' in d)
# # key = 'two'
#
# # if key in d:
# #     del d[key]
#
# # try:
# #     del d[key]
# # except KeyError:
# #     print("Такого элемента нет в словаре")
# # print(d)
#
# for key in d:
#     print(key, "->", d[key])
#

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить? ->"))
# del d[dislike]
# print(d)
# print(len(d))

# goods = {
#     "1": ["Core - i3 - 4330", 9, 4500],
#     "2": ["Core - i5 - 4670", 3, 8500],
#     "3": ["AMD FX - 6300", 9, 3700],
#     "4": ["Pentium G3230", 9, 2100],
#     "5": ["Core - i5 - 3450", 9, 4600],
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2],' рублей', sep="")
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         k = int(input('Количество'))
#         goods[n][1] = k
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2], ' рублей', sep="")

# d = {'A': 1, 'B': 2, "C": 3}
# v = d['B']
# print('B =', v)
# value = d.get('E', 'False')
# d.clear()
# d2 = d.copy()
#
# print('D =', d)
# print('D2 =', d2)
# print()
#
# d['E'] = 7
# d2['B'] = 5
#
# print('D =', d)
# print('D2 =', d2)

# d = {'A': 1, 'B': 2, "C": 3}
# # a = d.items()
# # print(a)
# # b = d.keys()
# # print(b)
# c = d.values()
# print(c)
#
# for key, val in d.items():
#     print(key, val)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#     },
#     'Second': {
#         4: 'four',
#         5: 'five',
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')

# sales = {
#     'John': {
#         "N": 3856,
#         "S": 8463,
#         "E": 8441,
#         "W": 2964,
#     },    'Tom': {
#         "N": 4832,
#         'S': 6786,
#         'E': 4737,
#         'W': 3612,
#     },    'Anne': {
#         'N': 5239,
#         'S': 4802,
#         'E': 5820,
#         'W': 1859,
#     },    'Fiona': {
#         'N': 3904,
#         'S': 3645,
#         'E': 8821,
#         'W': 2451,
#     }
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
# name = input('Имя: ')
# region = input('Регион: ')
# print(sales[name][region])
# new_pac = int(input('Новое значение: '))
# sales[name][region] = new_pac
# print(sales[name])

# data = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d = {v: k for k, v in data.items()}
# print(d)
# #ПОМЕНЯЛИ КЛЮЧИ И ЗНАЧЕНИЯ МЕСТАМИ

# data = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d = {v: k for k, v in data.items() if v <= 2}
# print(d)

# s = 'Hello'
# b = {i: i * 2 for i in s}
# print(b)
# a = list(b.values())
# print(a)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# new_a = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         new_a[i] = []
#         s = i
#     else:
#         new_a[s].append(i)
# print(new_a)

# zip() объединение словарей


# d = dict(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = {k: v for k, v in zip(a, b)}
# print(d)

# d = zip([12, 1, 2], ['Dec', 'Jan', 'Feb'])
# print(d)
# print(type(d))
# # print(dict(d))
# print(list(d))

# a = ['a', 'b', 'c', 'd']
# b = [12, 1, 2]
# c = [4.0, 5.0, 6.0]
# q = zip(a, b, c)
# # print(list(c))
# print(list(q))


# print(list(zip(range(5), range(100))))

# one = {'name': 'Igor', 'last_name': 'Smith', 'job': 'Consultant'}
# two = {'name': 'Olga', 'last_name': 'Doe', 'job': 'Manager'}
# three = {'name': 'Maks', 'last_name': 'Jon', 'job': 'Logist'}
# for (k1, v1), (k2, v2), (k3, v3) in zip(one.items(), two.items(), three.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)
#     print(k3, '->', v3)

# Распаковка последовательности
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# production_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, production_cost, month):
#     profit = sales - costs
#     print("Общая прибыль за", m, '=', profit)

# one = {'apple': 20, 'orange': 35}
# two = {'pepper': 40, 'onion': 55}
# print({**two, **one})

# for i in range(3):
#     print(i)
#
# color = ['red', 'yellow', 'green']
# j = 1
# for i in color:
#     print(j, i)
#     j += 1

# colors = ['red', 'yellow', 'green']
# for j, i in enumerate(colors, 1):
#     print(j, '=', i)

# num_list = [1, 2, 3, 4, 5]
# i = iter(num_list)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i, "STOP"))
# print(next(i, "STOP"))

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(2))
# print(func(2, 1, 3))
# print(func())

# def summa(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(7, 3))

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def ch(*args):
#     res = []
#     sr_ar = sum(args) / len(args)
#     print(sr_ar)
#
#     for i in args:
#         if i < sr_ar:
#             res.append(i)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

# def print_scores(student, *scores):
#     print("Srudent Name: " + student)
#     for score in scores:
#         print(score)
#
#
# print_scores("Irina", 100, 95, 88, 92, 99)
# print_scores("Igor", 96, 20, 33)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

# def intro(**data):
#     for key, value in data.items():
#         print(key, 'is', value)
#     print()
#
#
# intro(first_name="Irina", last_name='', age=22)
# intro(first_name="Igor", last_name='WOOD', email='igor1905@mail.ru', age=25, phone='9231435312')

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age='31', weight=61, eyes_color='gray')
# print('my_dict =', my_dict)

# def db(c, *args, name=None, **kwargs):
#     print(c, args, kwargs, name)
#
#
# db(6, 'q', 'w', 'e', a=5, name='Olga')

# name = 'Tom'
#
#
# def hi():
#     global name
#     name = 'Sam'
#     print('Hello', name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print('i =', i)
#     print(arg)
#
#
# i = 6
# func()


# def add_two(a):
#     x = 2
#
#     def add_some():
#         x = 5
#         print('x =', x)
#         return a + x
#
#     return add_some()
#
# print(add_two(3))

# import builtins
#
# names = dir(builtins)
#
# for i in names:
#     print(i)

# def outer_func(who):
#     def inner_func():
#         print("hello ", who)
#
#     inner_func()
#
#
# outer_func("world!")


# def func1():
#     a=6
#
#     def func2(b):
#         a = 4
#         print("Summa",a + b)
#
#     print("Znachenie peremennou a:", a)
#     func2(4)
#
# func1()

# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#             print("fn3.x =", x)
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)
# print(type(res))

# def increment(number):
#     def inner(x):
#         return number + x
#
#     return inner
#
#
# a = (increment(10))
# print(a(5))
# print(a(4))
#
# b = increment(1)
# print(b(7))
#
# print(increment(5)(10))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     a = 0
#
#     def inner():
#         nonlocal a
#         a += 1
#         print(city, a)
#
#     return inner
#
#
# res1 = func('Moscow')
# res1()
# res1()
# res1()
# res2 = func('Sochi')
# res2()
# res2()
# res1()
# res1()

# student = {
#     "Alice": 98,
#     "Bob": 67,
#     "Chris": 85,
#     "David": 75,
#     "Elice": 54,
#     "Fiona": 35,
#     "Grace": 69
# }
#
#
# def make_classifier(lower, upper):
#     def students(exem):
#         return {k: v for k, v in exem.items() if lower <= v < upper}
#
#     return students
#
#
# a = make_classifier(80, 100)
# b = make_classifier(70, 80)
# c = make_classifier(50, 70)
# d = make_classifier(0, 50)
#
# print(a(student))
# print(b(student))
# print(c(student))
# print(d(student))

# figure_type = ('rhombus', d1 = 10, d2 = 8)
#
# def exept(**kwargs):
#     return {k: v for k, v in kwargs.items()}

# //////////////ПАРА №15//////////////////////////
# lambda (анонимные функции)
# print((lambda x, y: x + y)(1, 2))
#
#
# # Обычная функция
# def get_sum(x, y):
#     return x + y
#
#
# print(get_sum(1, 2))

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(3, 4))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func(3, 4))


# print((lambda x, y: x * x + y * y)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ(a=3))
# print(summ(10, 10, 10))

# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4, 5, 6, 7))
# print(func1('a', 'b', 'c'))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# f = inc(5)
# print(f(2))

# def inc1(n):
#     return lambda x: n + x
#
#
# f1 = inc1(5)
# print(f1(2))
#
#
# print((lambda n: lambda x: x + n)(5)(2))


# print((lambda n: lambda x: lambda y: x + n + y)(10)(5)(2))


# d = {'b': 10, 'a': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1], reverse=True)
# print(list_d)
# print(dict(list_d))


# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'raiting': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['last_name'])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(res2)
#
# res3 = sorted(players, key=lambda item: item['raiting'])
# print(res3)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# b = a[0](5, 3)
# c = a[1](5, 3)
# d = a[2](5, 3)
# f = a[3](5, 3)
# print(b)
# print(c)
# print(d)
# print(f)


# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, "three": lambda x: x}
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
# }
# d[3]()


# print((lambda a, b: a if a > b else b )(15, 4))
# #a if a > b else b - это тернарное выражение

# ФУНКИЦ map(func,*iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# a = list(map(mult, lst))
# print(a)
#
# print(list(map(lambda t: t * 2, lst)))


# b = ['1', '2', '3', '4', '5']
# # c = list(map(int, b))
# # print(c)

#
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: (x, y), st, num)))


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: (x + y), l1, l2)))


# ФУНКИЦ filter(func,*iterables)- возвращает значение True или False

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda i: i > 75, b))
# print(res)


# import random
#
# s = [random.randint(1, 40) for i in range(10)]
# print(s)
# print(list(filter(lambda x: 10 <= x <= 20, s)))
#


# Декораторы


# def hello():
#     return 'hello,i am func "hello"'
#
#
# def super_func(func):
#     print('hello, i am func "super_func"')
#     print(func())
#
# super_func(hello)


# def hello():
#     return 'hello,i am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func): # 2
#     def func_wrapper():  # 3
#         print('Code before') # 4
#         func() # 5
#         print('Code after') # 8
#     return func_wrapper # 3
#
#
# def func_test():  # 6
#     print('func_test') # 7
#
#
# text = my_decorator(func_test)  #1
# text()


# def my_decorator(func): # Декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()  # 5
#         print('*' * 40)
#
#     return func_wrapper
#
#
# @my_decorator # Декоратор
# def func_test():  # Декорируемая функция
#     print('func_test')
#
# @my_decorator
# def hello():
#     print('hello')
#
#
#
# func_test()
# print()
# hello()
# # text = my_decorator(func_test)
# # text()


# Декоратор это функция которая разворачивает другую функцию для расширения функционала, не изменяя саму функцию

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())

# def cnt(fn):
#     i = 0
#     def wrap():
#         nonlocal i
#         i += 1
#         fn()
#         print('Вызов функции: ', i)
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(args1, args2):
#         print("Данные:", args1, args2)
#         fn(args1, args2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут:', first, last)
#
#
# print_full_name('Ирина', 'Лаврова')


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# @args_decorator
# def new_func(q):
#     print(q)
#
#
# print_full_name('Борис', 'Елизавета', "Светлана", study='JavaScript')
# print_full_name('Максим', 'Екатерина', "Дмитрий")
# new_func('Новая функция')

# def decor(args1, args2):
#     def args_decorator(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_decorator
#
#
# @decor("Сложение:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Вычитание:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(2, 4)
# sub(5, 2)


# def multiply(arg):
#     def my_dec(fn):
#         def wrap(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return wrap
#
#     return my_dec
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print("Результат:", return_num(5))


# print(int('100', 2))
# print(int('100', 10))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(18))
# print(oct(18))
# print(hex(18))

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
#
# print(e * 3)
# print(e * -3)
#
# print(e in "I am learn Python")
# print(e in "I am learn Java")


# s = "Hello"
# print(s[1])
# print(s[-5])
# print(s[4])
# print(s[1:3])
# print(s[::-1])


# s = 'python'
# s = s[:3] + 't' + s[4:]
# print(s)

# def changeCharToStr(s, c_old, c_new):
#     i = 0
#     s2 = ''
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = changeCharToStr(str1, 'N', 'P')
# print(str1)
# print(str2)

# ПРЕФИКСЫ
# print(u'Hello')
# print('Hello')

# print('I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt') # r - роу строки(игнорирует экронирование)
# print(r'C:\file\\'[:-1])
# print(r'C:\file' + '\\')
# print('C:\\file\\')


# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name} мне {age} лет')

# import math
# print(f'Значение числа pi: {round(math.pi, 2)}')
# print(f'Значение числа pi: {math.pi:.2f}')

# x = 10
# y = 5
# print(f"{x} * {y} / 2 = {x * y / 2}")


# a = 74
# print(f"{{{a}}}")


# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")


# s = 'Hello'
# print(s)
#
# a = """aaa"""
# print(a)
#
# """Hel
# lo"""
#
# '''aa
# aa'''


# s = '''
# <div>
#     <a href="#">content<a/>
# </div>'''
#
# print(s)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     a = 2
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__) # вызов документации функции


# import math as m
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
#
# print(cylinder(2, 4))

# print(ord('a'))
# print(ord('#'))
# print(ord('k'))
#
#
# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# arr = [ord(i) for i in my_str]
# print('ASCII коды: ', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [i for i in [ord(i) for i in input('->')[:3]] if i not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print('Количество последних элементов:', arr.count(arr[-1]) -1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(7897))
# print(chr(33))

# from random import randint
#
# short = 7
# longest = 12
# min_ascii = 33
# max_ascii = 126


# def random_password():
#     random_lenght = randint(short, longest)
#     res = ''
#     for i in range(random_lenght):
#         random_char =chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль: ", random_password())


# s = 'hello, WORLD! I am learn Python.'
# print(s.capitalize()) #Hello, world! i am learn python.
# print(s.lower()) #hello, world! i am learn python.
# print(s.upper()) #HELLO, WORLD! I AM LEARN PYTHON.
# print(s.swapcase()) #HELLO, world! i AM LEARN pYTHON.
# print(s.title()) #Hello, World! I Am Learn Python.


# s = 'hello, WORLD! I am learn Python.'
# print(s.count('h')) # метод считает сколько встречается букв в тексте
# print(s.count('h', 1, -4)) # с ограниченным поиском
# print(s.find('Python')) # находит индекс слова в предложении(первая буква),если возвращает -1 то элемент не найден


# string = 'один два'
# one = string[:string.find(' ')]
# two = string[string.find(' ') + 1:]
# print(two + " " + one)


# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '0123456789'.find(i) != -1:
#         digits.append(int(i))
# print(digits)


# s = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# int1 = s.index('(')
# int2 = s.index(')')
# print(int1)
# print(int2)
#
# print(s[int1 + 1:int2])

# s = 'hello, WORLD! I am learn Python.'
# print(s.find('l'))
# print(s.rfind('l'))
# print(s.index('l'))
# print(s.rindex('l'))


# s = 'Some content in this message has been blocked because the sender ' \
#     'isnt, in your Safe senders list'
# item = 'o'
# if s.count(item) == 1:
#     print(s.find(item))
# elif s.count(item) >= 2:
#     print(s.find(item), s.rfind(item))


# s = 'hello, WORLD! I am learn Python.'
# print(s.endswith('on.'))
# print(s.endswith('lo', 3, 5))


# print('aab123'.isalnum()) # не пустая и состоит только из букв или цифр

# print('ABCabc'.isalpha()) # не пустая и содержит только буквы

# print('1234'.isdigit()) # не пустая и содержит только цифры

# print('abc'.islower()) # не пустая и состоит из элементов нижнего регистра

# print('ABC'.isupper()) # не пустая и состоит из элементов верхнего регистра

# print(' \t \n '.isspace()) # строка состоит только из пробельных символов + табуляция и перенос


# Метод визуального форматирования

# print('py'.center(10))
# print('py'.center(10, '-'))
# print('py'.center(2, '-'))


# print("     py".lstrip())
# print('py     '.rstrip())
# print('    py    '.strip())
#
# print('https://www.python.org/'.lstrip('th/ps:'))
# print('https://www.python.org/'.lstrip('th/ps:').rstrip('/.org'))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace('Nython', 'Python', 2))


# s = "-"
# seq = ("a", 'b', "c")
# print(s.join(seq)) # a - b - c
#
# print("..".join(['1', '2'])) # 1..2
# print(':'.join('Hello'))
#
# print('Строка разделенная пробелами'.split())
# print('www.python.org.ru'.split('.', 2))
# print('www.python.org.ru'.rsplit('.', 2))
# print('www...python...org.ru'.split('.'))


# a = input('->').split()
# print(a)
# print(a[2])


# def name(name):
#     print(f"{name[0]} {name[1][0]}.{name[2][0]}.")
#
#
# FIO = input('Введите ФИО: ').split()
# name(FIO)


# s = 'В строке заменить пробелы символом'
# lst = s.split()
# print(lst)
# st = '*'.join(lst)
# print(st)
#
# print(s.replace(' ', '*'))


# Регулярные выражения ///////////
# Методы со строками//////////////

# s = "Я ищу совпадения в 2021 году. И я из найду в 2 счёта."
# reg = 'я' # шаблон(то что ищем в строке)
# print(s.find(reg))
# print(re.findall(reg, s)) # возвращает список содержащий все совпадения
# print(re.search(reg, s)) # возвращает первый найденный элемент совпадения
# print(re.search(reg, s).span()) # (15,16)
# print(re.search(reg, s).start()) # (15)
# print(re.search(reg, s).end()) # (16)
# print(re.search(reg, s).group()) # (я)
#
# print(re.match(reg, s)) # Ищет только в начале строки
#
# print(re.split(reg, s, )) # заменяет на символ разделитель, и возвращает список
# print(re.split(reg, s, 1)) # заменяет на символ разделитель, и возвращает список


# Замена текста на то что укажем
# s = "Я ищу совпадения в 2021 году. И я из найду в 2 счёта."
# reg = 'я' # шаблон(то что ищем в строке)
# print(re.sub(reg, "!", s)) # (что заменяем,на что меняем, где меняем)
# print(re.sub(reg, "!", s, 1)) # 1 - замена только первого элемента


# s = "Я ищу совпадения в 2021 году. И я из найду в 2 счёта."
# s2 = "Я ищу [совпадения] в 2021 году. И я из найду в 2 счёта."
# s2 = "Я ищу [совпадения] в 2021 го-ду. И я из найду в 2 счёта."
# # reg = r'[2021]'
# #[] - любой из символов
# # print(re.findall(reg, s))
#
#
# reg = r'[0-9]'# выводит все значение попавшие в диапозон от 0 до 9
# reg2 = r'[а-я]'
# reg3 = r'[ёа-я]'
# reg4 = r'[А-яё.\[\]]'
# reg5 = r'[А-яё.\[\]-]'
# print(re.findall(reg, s))
# print(re.findall(reg2, s)) # нет буквы ё
# print(re.findall(reg3, s))
# print(re.findall(reg4, s2))
# print(re.findall(reg5, s2))


# s = "Я ищу совпадения в 2021 году. И я из найду в 2 счёта."
# reg = r'[А-яё.\[\]-]'
# reg1 = r'[^0-9]' # ^ - все кроме цифр от 0 до 9
# print(re.findall(reg1, s))

# s = 'Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09.'
# reg = '[0-2][0-2]:[0-5][0-9]'
# print(re.findall(reg, s))


# s = "Я ищу совпадения в 2021 году. И я из найду в 2 счёта.45678"
# reg1 = r'.'  # возвращает все символы буквы и цифры
# reg2 = r'\.' # возвращает только точки с предложения
# reg3 = r'\d' # \d одна цифра [0-9]
# reg4 = r'\w' # \w цифра, буква, символ _ [0-9А-яA-z_]
# reg5 = r'\s' # \s выводит все пробелы, табуляции, перенос строки
# reg6 = r"\w+" # + - от 1 до бесконечности повторений
# reg7 = r'20*' # * - от 0 до бесконечности повторений
# print(re.findall(reg7, s))
#
# d = "Цифры: 7, +17, -42, 0013, 0.3"
# reg1 = r'[+-]?[\d.]+'   # ? - 0 или 1
# print(re.findall(reg1, d))


# s = '05-03-1987 # Дата рождения'
# print('Дата рождения: ', re.sub("-", '.', re.sub("#.*", '', s)))


# s = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg, s))


# s = "12 сентября 2021 года"
# reg = r'\d{2,4}'
# print(re.findall(reg, s))

#
# s = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'[0-9]+[^А-я]+', '12 + й'))

#
# text = "hello world"
# print(re.findall(r'\w+', text, flags=re.DEBUG))


# text = """
# one
# two
# """
#  print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))


# text = """
# Python,
# python,
# PYTHON
# """
# reg = '(?mi)^python'
# print(re.findall(reg, text))


# def validate_name(name):
#     return re.findall(r'[\w-]{3,16}', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))

# greedy - захватывает максимально возможное число символов
# ? - lazy - захватывает минимально возможное число символов

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.*>', text))

# s = '<p>Изображение <img alt="картинка" src="bg.jpg"> - фон страницы</p>'
# reg = '<img[^>]*>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))


# text = 'Методы этой группы[16] выполняют[17] преобразование регистра[18][19] строки'
# print(re.findall(r'\[.*?]', text))


# s = 'Петр, Ольга и Виталий отлично учатся'
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))


# s = 'int = 4, float = 4.0, double = 8.0f'
# reg = r"(?:int|float)\s*=\s*\d[.\w]*"
# print(re.findall(reg, s))
# # (?: ...) - обозначает, что это группирующая скобка является не сохраняющей


# s = '28-08-2021'
# reg = '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9]|20[0-9][0-9])'
# print(re.findall(reg, s))


# s = 'Я ищу совпадения в 2021 года. И я из найду в 2 счёта'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])
# print(re.findall(reg, s))


# text = """
# Самара
# Москва
# Сочи
# Тверь
# Уфа
# Казань
# """


# count = 0
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
# print('<select>')
# print(re.sub(r'\s*(\w+)\s*', replace_find, text))
# print('</select>')


# s = '<p>Изображение <img src="bg.jpg"> - фон страницы</p>'
# # reg = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q)>'
# # (?P<name>) (?P=name)
# print(re.findall(reg, s))


# s = "Самолет прилетает 10/23/2022. Будем рады вас видеть после 10/24/2022"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# # print(re.findall(reg, s))
# print(re.sub(reg, r'\2.\1.\3', s))


# s = "google.com and google.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# # print(re.findall(reg, s))
# print(re.sub(reg, r"http://\1", s))


# def validate(name):
#     reg = r"^\+?7[ (]*\d+[ )]*[\d -]{8,10}$"
#     return re.search(reg, name).group()
#
#
# print(validate('+7 499 456-45-78'))
# print(validate('+74994564578'))
# print(validate('7 (499) 456 45 78'))
# print(validate('7 (499) 456-45-78'))

# /////////////////20 ПАРА//////////////////////////
# Рекурсия -  когда функция сама себя вызывает


# def elevator(n):   # n - номер этажа
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print('=>', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('На каком Вы этаже: '))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# МЕТОД РЕКУРСИИ
# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0]
#     else:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0] + sum_list(lst[1:])


# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = '0123456789'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base] #6 5
#
#
# print(to_str(356, 2))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list)) # False
# print(names[1])
# print(isinstance(names[1], list)) # True
# print(names[1][1])
# print(isinstance(names[1][1], list)) # True
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list)) # True

# Функция с методом рекурсии
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# Функция без рекурсии


# def func(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i,list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count +=1
#                 else:
#                     count +=1
#             else:
#                 count +=1
#     return count
#
#
#
# print(func(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == " " or text[0] == "!":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:]) # Hello
#
#
# print(remove(" Hello\tWorld! "))

# Файлы

# f = open(r'C:\Users\79969\PycharmProjects\pythonProject1\text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()

# print(f.readline())
# print(f.read())

# print(f.readlines())


# f = open(r'C:\Users\79969\PycharmProjects\pythonProject1\text.txt', 'r')


# 1 способ считывания кол-во строк
# print(len(f.readlines()))
# f.close()

# 2 способ считывания кол-во строк
# cnt = 0
# for line in f:
#     cnt += 1
# f.close()


# 3 способ считывания кол-во строк
# cnt = 0
# s = f.readline()
# while s != '':
#     s = f.readline()
#     cnt += 1
#
# print(cnt)
# f.close()


# f = open('xyz.txt', 'w')
# f.write('Hello World!')
# f.close()


# f = open('xyz.txt', 'a')
# # f.write('Hello World!')
# f.write('\nNew text')
# f.close()


# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# my_file = open('text2.txt', 'w')
# my_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# my_file.close()
#
# my_file = open('text2.txt', 'r')
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello World!\n"
#
# print(read_file)
# my_file.close()
# my_file = open('text2.txt', 'w')
# my_file.writelines(read_file)
# my_file.close()

#####DZ20#########//////////////////////
# def kol_list(item):
#
#     count = 0
#     for i in range(item):
#         if i > 0:
#             print(i)
#             count += 1
#         return count
#
#
# print(kol_list([-2, 3, 8, -11, -4, 6]))
#####DZ20#########//////////////////////


# my_file = open('text3.txt', 'w')
# my_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# my_file.close()
#
# my_file = open('text3.txt', 'r')
# read_file = my_file.readlines()
# print(read_file)
# pos = int(input("Введите индекс удаления строки: "))
# if 0 <= pos <= len(read_file):
#     del read_file[pos]
# else:
#     print('Индекс введен не верно!')
# print(read_file)
# my_file.close()
# my_file = open('text3.txt', 'w')
# my_file.writelines(read_file)
# my_file.close()


# f = open('text2.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()


# f = open('text.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# print(f.write('-PYTHON-'))
# print(f.tell())
# f.close()


# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line)


# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# print(get_line(lst))
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
# print("Done!")


# file_name = 'res.txt'
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# num_list = list(map(float, nums.split()))
# print(num_list)
# print(len(num_list))

# with open('text4.txt', 'r') as f:
#     w = f.read().split()
#     print(w)
#     max_length = len(max(w, key=len))
#     # max_length = max(len(world) for world in w)
#     print(max_length)
#     res = [word for word in w if len(word) == max_length]
#     print(res)


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)
#
# with open(write_file, 'w') as fw:
#     for line in fr:
#         print(line)


# f = open('text4.txt', 'r')
# line = 0
#
# for i in f:
#     line += 1
#     word = 0
#     flag = 0
#     for j in i:
#         if j != ' ' and flag == 0:
#             word += 1
#             flag = 1
#         elif j == ' ':
#             flag = 0
#     print(i, len(i), 'символов', word, 'слов')
# print(line, 'строки')
# f.close()

# ////////////////////////////////////////////////////////////
# модуль os и os.path
# для работы с директориями и файлами

# print('Текущая директория:', os.getcwd())
# print(os.listdir()) #вернулся список файлов, находящийся в текущей директории
# # директории по указанному пути
# print(os.listdir(".."))

# os.mkdir('folder') # создает папку с названием в (" название папки ")

# os.makedirs('nested1/nested2/nested4') # создает папки внутри папок(вложенные папки)

# os.remove('xyz') # удаление файла
#
# os.rename('nested1', 'test') # переименование файла,папки и т.д..Первый параметр название файла,на что переименовываем

# os.rename('test.txt', 'test/test1.txt') # переменование с перемещением файла
# # ('название файла', 'путь перемещения/новое имя файла')

# os.renames('text.txt', 'text/text1.txt')

# os.rmdir('folder') # удаление пустой папки

# for root, dirs, files in os.walk('test'):
#     print('Root:', root)
#     print('\tSubdirs:', dirs)
#     print('\tFiles:', files)


# Удаление пустых директорий в ветви Work

# def remove_empty_dirs(root_three):
#     for root, dirs, files, in os.walk(root_three):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удаленна.")
#
#
# remove_empty_dirs("test")
# import os.path
#
# print(os.path.split(r"C:\Users\79969\PycharmProjects\pythonProject1\test\test1.txt"))
# # разбивает путь на кортеж(head, tail)
#
# print(os.path.dirname(r"C:\Users\79969\PycharmProjects\pythonProject1\test\test1.txt"))
# print(os.path.basename(r"C:\Users\79969\PycharmProjects\pythonProject1\test\test1.txt"))

# os - операционная система

# print(os.path.join(r'C:\Users\79969', 'PycharmProjects', 'pythonProject1', 'test1.txt'))

# Написать программу,которая создаст приведенное на рисунке дерево директории
# и файлов
# dirs = ['Work/F1', 'Work/F2/F21']
# # for dir in dirs:
# #     os.makedirs(dir)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# for k, v in files.items():
#     for file in v:
#         file_path = os.path.join(k, file)
#         print(file_path)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt',
#                   r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f'Некоторый текст в файле {file}.')
#
#
# def print_three(root, topdown):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs , files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
# print_three('Work', topdown=False)
# print_three('Work', topdown=True)

# print(os.path.exists(r'C:\Users\79969\PycharmProjects\pythonProject1\test1.txt'))
# path = 'test1.txt'
# print(os.path.getatime(path))
# print(os.path.getmtime(path))
# print(os.path.getctime(path))
# print(os.path.getsize(path))

# path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.3\plugins\python-ce\helpers\typeshed\stdlib\builtins.pyi"
#
# size = os.path.getsize(path)
# kb_size = size // 1024
# print("Размер: ", kb_size, 'KB')
# c_time = os.path.getctime(path)
# print(c_time)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c_time)))

# print(os.path.isfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.3\plugins\python-ce\helpers\typeshed\stdlib\builtins.pyi"))
# print(os.path.isdir(r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.3\plugins\python-ce\helpers\typeshed\stdlib"))

# ООП (объектно ориентированное программирование) - это парадигма программирования

# Парадигмы ООП:
# инкапсуляция - сокрытие данных(запрет на получение данных из вне)
# наследование - создавать что-то на основе родительского контроля
# полиморфизм - название одинаковое но ведут себя по разному в зависимости от ситуации


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 200
# p1.y = 5
# p1.set_coords()
# Point.set_coords(p1)
#
#
# p2 = Point()
# p2.set_coords()
#
# # Point.x = 100
# # p2 = Point()
# # print(type(p1))
# # print(p1.x, p1.y)
# # print(id(p1.x))
# # print(id(Point))
# # print(p1.__dict__)
# # print(p2.__dict__)
# # print(Point.__dict__)
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))


# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coords(5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coords(3, 8)
# print(p2.__dict__)


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '0-000-000-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\n'
#               f'Дата рождения: {self.birthday}\n'
#               f'Номер телефона: {self.phone}\n'
#               f'Страна: {self.country}\n'
#               f'Город: {self.city}\n'
#               f'Домашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
# h1 = Human()
# h1.input_info('Юля', "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name('Валерия')
# print(h1.get_name())
# h1.set_birthday("21.01.1993")
# print(h1.get_birthday())


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# print(p1.__dict__)
# print(p1.x)
# print(getattr(p1, 'x'))
# print(getattr(p1, 'z', "no"))
# print(hasattr(p1,'z'))
# print(hasattr(p1, 'y'))
# setattr(p1, 'z', 7)
# print(getattr(p1, 'z', "no"))
# print(p1.__dict__)


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, '\n')
#
#
# p1 = Person("Victor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dilgih")
# p2.print_info()
# p2.add_skill(2)
#
# print(p1.__dict__)
# print(p2.__dict__)


# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("This is constructor!")
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("This is initializator!")
#
# p1 = Point()


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('Удаление экземпляра:' + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)


# class Point:
#     count = 0 # Статические свойства
#
#     def __init__(self, x=0, y=0): # Динамические свойства
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(15, 20)
# p3 = Point(1, 20)
# print(Point.count)
# print(p2.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота: ", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, 'был последним!')
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print('Численность роботов:', droid1.k)
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print('Численность роботов:', droid2.k)
# droid3 = Robot("R3-С6")
# droid3.say_hi()
# print('Численность роботов:', droid3.k)
#
# print("\nЗдесь роботы могут проделывать какую-то работу \n")
#
# print("Роботы закончили свою работу. Давайте их выключим!")
# del droid1
# del droid2
# del droid3
# print('Численность роботов:', Robot.k)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def set_coords(self, x, y):
#         if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами!")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 100)
# p1.set_coords(1, 2)
# print(p1.get_coords())
# # p1.__x = 100
# # p1.__y = 50
# # print(p1.__x, p1.__y)
# print(p1.__dict__)


# class Car:
#     def __init__(self, name, year, model, power, color, price):
#         self.__name = self.__model = self.__color = 'Некорректные данные'
#         self.__year = self.__power = self.__price = 0
#         if Car.__check_value_str(name):
#             self.__name = name
#         if Car.__check_value_int(year):
#             self.__year = year
#         if Car.__check_value_str(model):
#             self.__model = model
#         if Car.__check_value_int(power):
#             self.__power = power
#         if Car.__check_value_str(color):
#             self.__color = color
#         if Car.__check_value_int(price):
#             self.__price = price
#
#     def __check_value_int(s):
#         if not isinstance(s, int):
#             print('Данные должны быть числом')
#             return False
#         return True
#
#     def __check_value_str(s):
#         if not isinstance(s, str):
#             print('Данные должны быть строкой')
#             return False
#         return True
#
#     def set_name(self, name):
#         if Car.__check_value_str(name):
#             self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def print_info(self):
#         print("Данные автомобиля".center(40, '*'))
#         print(f'''Название модели: {self.__name}
# Год выпуска: {self.__year}
# Производитель: {self.__model}
# Мощность двигателя: {self.__power} л.с.
# Цвет машины: {self.__color}
# Цена: {self.__price}
# ''')
#
#
# c1 = Car('X7 M50i', 2021, 'BMW', 530, 'white', 10790000)
# c1.print_info()
# c1.set_name('X2')
# c1.print_info()
# print(c1.get_name())


# class Point:
#     __slots__ = ['x', 'y', 'z']
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 2
# print(p1.z)
# # print(p1.__dict__)


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print('Вызов __set_x')
#         self.__x = x
#
#     def __get_x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coord_x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x
# print(p1.__dict__)


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def coord_x(self):  # get
#         print("Вызов __get_x")
#         return self.__x
#
#     @coord_x.setter
#     def coord_x(self, x):  # set
#         print('Вызов __set_x')
#         self.__x = x
#
#     @coord_x.deleter
#     def coord_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x
# print(p1.__dict__)


# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def info_name(self):
#         return self.__name
#
#     @info_name.setter
#     def info_name(self, name):
#         self.__name = name
#
#     @info_name.deleter
#     def info_name(self):
#         del self.__name
#
#     @property
#     def info_age(self):
#         return self.__age
#
#     @info_age.setter
#     def info_age(self, age):
#         self.__age = age
#
#     @info_age.deleter
#     def info_age(self):
#         del self.__age
#
#
# p1 = Person('Irina', '26')
# print(p1.__dict__)
# p1.info_name = 'Igor'
# p1.info_age = '31'
# print(p1.__dict__)
# del p1.info_name
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
# p1 = Point()
# print('p1 =', Point.get_count())
# p2 = Point()
# print('p2 =', Point.get_count())
# p3 = Point()
# print('p3 =', Point.get_count())
#
# print(Point.get_count())


# class numbers:
#     @staticmethod
#     def min(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def max(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def sr_ar(a, b, c, d):
#         sr_ar = (a + b + c + d) / 4
#         return sr_ar
#
#     @staticmethod
#     def factor(a):
#         count = 1
#         for i in range(1, a + 1):
#             count = count * i
#         return count
#
#
# print("Минимальное число: ", numbers.min(4, 5, 3, 9))
# print("Максимальное число: ", numbers.max(4, 5, 3, 9))
# print("Среднее аривметическое: ", numbers.sr_ar(4, 5, 3, 9))
# print("Факториал: ", numbers.factor(5))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#     @classmethod
#     def from_string(cls, data_as_string):
#         d, m, y = map(int, data_as_string.split('.'))
#         return cls(d, m, y)
#
#     @staticmethod
#     def is_date_valid(data_as_string):
#         if data_as_string.count('.') == 2:
#             d, m, y = map(int, data_as_string.split('.'))
#             return d <= 31 and m <= 12 and y <= 3999
#
#
# dates = [
#     '30.12.2020',
#     '30.12.2020',
#     '21.01.2021',
#     '12.11.2020'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print('Некорректная дата', string_date)

# string_date = '20.10.2022'
#
# date1 = Date(20, 10, 2022)
# print(date1.string_to_db())
#
# date2 = Date.from_string('30.04.2021')
# print(date2.string_to_db())
#
# date3 = Date.from_string('35.40.2021')
# print(date3.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print("*" * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счёт с #{self.num} принадлежащий {self.surname} был закрыт!')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print(f'Информация о счете:')
#         print("-" * 30)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print("-" * 30)
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у Вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} внесены на баланс!')
#         self.print_balance()
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
# acc.add_percents()
# print()
#
# acc.withdraw_money(500)
# print()
# acc.add_money(5000)


# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.__fio = fio.split()
#         self.__old = old
#         self.__ps = ps
#         self.__weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for i in f:
#             if len(i.strip(letters)) != 0:
#                 raise TypeError('Неверный формат ФИО')
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет.")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (float, int)) or w < 20:
#             raise TypeError("Вес должен быть числом от 20 кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат папортных данных")
#         for i in s:
#             if not i.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def ps(self):
#         return self.__ps
#
#     @ps.setter
#     def ps(self, ps):
#         self.verify_ps(ps)
#         self.__ps = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserData('Волков Игорь Николаевич', 26, '1234 560090', 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# p1.old = 21
# p1.ps = "2313 424323"
# p1.weight = 45
# print(p1.__dict__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x},{self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         print('Родительский инициализатор Prop')
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('Переопределенный инициализатор Line')
#         super().__init__(*args)  # передаем переменные с родительского инициалитора
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии:{self._sp},{self._ep}, {self._color},{self.get_width()}')
#
#
# class Rect(Prop):
#
#     def __init__(self, sp, ep, color='red', width=1, bg='yellow'):
#         super().__init__(sp, ep, color, width)  # передаем переменные с родительского инициалитора
#         self.bg = bg
#
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника:{self._sp},{self._ep}, {self._color},{self.get_width()},{self.bg}')
#
#
# line = Line(Point(1, 2), Point(10, 20), 'green', 3)
# # print(line.draw_line())
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         if w > 0:
#             self.__width = width
#         else:
#             # self.__width = 0
#             raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         if height > 0:
#             self.__height = height
#         else:
#             raise ValueError
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.width)

#
# class Rect:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height} ')
#
#
# class RectFon(Rect):
#     def __init__(self, w, h, bg):
#         super().__init__(w, h)
#         self.fon = bg
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка: {self.fon}')
#
#
# class RectBorder(Rect):
#     def __init__(self, w, h, px):
#         super().__init__(w, h)
#         self.px = px
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка: {self.px}')
#
#
# shape1 = RectFon(400, 200, 'red')
# shape1.show_rect()
#
# shape2 = RectBorder(600, 300, '1px solid red')
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3, 4, 5])
# print(v)
# print(type(v))
# q = Vector([6, 7, 8, 9, 10])
# print(q)


# Перегрузка методов

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x},{self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print('Координаты должны быть числами')
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print('Координаты должны быть целочисленными')
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#
# class Line(Prop):
#     def draw_line(self) -> None:
#         print(f'Рисование линии:{self._sp},{self._ep}, {self._color},{self._width}')
#
#     def set_coords(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10, 20), Point(100, 200))
# line.draw_line()
#
# line.set_coords(Point(-10, -20))
# line.draw_line()


# Абстрактные методы

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x},{self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print('Координаты должны быть числами')
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print('Координаты должны быть целочисленными')
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#     def draw(self): # Абстрактный метод(виртуальный метод)
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self) -> None:
#         print(f'Рисование линии:{self._sp},{self._ep}, {self._color},{self._width}')
#
#
# class Rect(Prop):
#     pass
#     # def draw(self) -> None:
#     #     print(f'Рисование прямоугольника:{self._sp},{self._ep}, {self._color},{self._width}')
#
#
# class Elips(Prop):
#     def draw(self) -> None:
#         print(f'Рисование эллипса:{self._sp},{self._ep}, {self._color},{self._width}')
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Elips(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             # self._width = width
#             # self._length = length
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):  # Абстрактный метод
#         raise NotImplementedError('В дочернем классе должен быть определен метод calc_area()')
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t1 = SqTable(20, 10)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t = SqTable(20)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())


# Абстрактные классы
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print('Метод move() в базовом классе')
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print('*' * 30)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print('*' * 30)
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')


# Интерфейс - это внешние элементы которые должны быть видны, могут быть только абстрактные методы


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('Я метод внешнего класса')
#
#     def outer_obj_method(self):
#         print('Обычный метод')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Я метод внутренного класса', MyOuter.age)
#             MyOuter.outer_class_method()
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print(f'name: {self.name}')
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print(f'name: {self.name}')
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()


# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Imployee List:')
#         print(f'Name: {self.name}')
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '123'
#
#         def display(self):
#             print(f'Name: {self.name}')
#             print(f'Id: {self.id}')
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '324'
#
#         def display(self):
#             print(f'Name: {self.name}')
#             print(f'Id: {self.id}')
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Class Outer')
#
#
#     class Inner:
#         def __init__(self):
#             self.innerclass = self.InnerClass()
#
#         def show(self):
#             print('Class Inner')
#
#         class InnerClass:
#             def show(self):
#                 print('Class InnerClass')
#
#
# outer = Outer()
# outer.show()
# inner1 = outer.inner
# inner1.show()
# inner2 = outer.inner.innerclass
# inner2.show()


# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def processor(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.model())

#
# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('Базовый класс')
#
#     class Inner:
#         def display1(self):
#             print('Вложенный класс в базовый')
#
#
# class Sub_class(Base):
#     def __init__(self):
#         print('Дочерний класс')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Вложенный класс в дочерний')
#
#
# a = Sub_class()
# a.display()
#
# # b = a.db
# b = Sub_class.Inner()
# b.display1()
# b.display2()


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# b = Dog('Buddy')
# b.sleep()
# b.play()
# b.bark()


# class A:
#     # def __init__(self):
#     #     print("Инициализатор класса А")
#     def hi(self):
#         print(A)
#
# class AA:
#     def hi(self):
#         print(AA)
#
# class B(A):
#     # def __init__(self):
#     #     print("Инициализатор класса B")
#     def hi(self):
#         print(B)
#
# class C(A):
#     # def __init__(self):
#     #     print("Инициализатор класса C")
#     def hi(self):
#         print(C)
#
# class D(B, C):
#     # def __init__(self):
#     #     B.__init__(self)
#     #     C.__init__(self)
#     #     print("Инициализатор класса D")
#     def hi(self):
#         print(D)
#
# d = D()
# print(D.mro())
# print(D.__mro__)
# d.hi()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x},{self.y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1, *args):
#         print('Инициализатор Styles')
#         self._color = color
#         self._width = width
#         super().__init__(*args)
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
#
#
# class Line(Styles, Pos):
#     def draw(self):
#         print(f'Рисование линии:{self._sp},{self._ep},{self._color},{self._width}')
#
#
# l1 = Line(Point(10, 20), Point(100, 100), 'red', 2)
# l1.draw()
# print(Line.__mro__)


# Миксим (примеси)

# class Displayer:  # родительский класс
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:  # миксин класс(Mixin)
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubClass()
# subclass.display('Эта строка будет отображаться и записываться в файл')


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print('Инициализатор Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog: #миксин-дополнительный функционал который можно применит к любому классу
#     ID = 0
#
#     def __init__(self):
#         print('Инициализатор MixinLog')
#         self.ID += 1
#         self.id = self.ID
#
#     def save_log(self):
#         print(f'{self.id}: товар был продан в 00:00 часов')
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook('HP', 1.5, 35000)
# n.print_info()
# n.save_log()


# Перегрузка операторов

# 24*60*60 = 86400 (число секунд в одном дне)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом данных Clock')
#         return Clock(self.sec // other.sec)
#
#     def __eq__(self, other):
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def get_format_time(self):
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise TypeError('Ключ должен быть строкой')
#
#         if item == 'hour':
#             return (self.sec // 3600) % 24
#         elif item == 'min':
#             return (self.sec // 60) % 60
#         elif item == 'sec':
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# с1['hour'] = 12
# print(c1['hour'], c1['min'], c1['sec'])
# c2 = Clock(100)
# print(c2.get_format_time())
# # c3 =c2 // c1
# # print(c3.get_format_time())
#
# if c1 > c2:
#     print('Время равно')
# if c1 != c2:
#     print("Время не равно")


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item <= len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть целым не отрицательцым числом')
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([0] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым не отрицательцым числом')
#
#         del self.marks[key]
#
# s1 = Student('Roman', [4, 2, 2, 5, 2])
# print(s1[2])
# s1[16] = 4
# del s1[2]
# print(s1.marks)


# Полиморфизм - способность системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта
# Простыми словами - возможность работать разными объектами языка Питон единым образом

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.h + self.w)
#
#
# class Square:
#     def __init__(self, x):
#         self.x = x
#
#     def get_perimetr(self):
#         return 4 * self.x
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for i in shape:
#     print(i.get_perimetr())
#     # if isinstance(i, Rectangle):
#     #     print(i.get_per_rect())
#     # else:
#     #     print(i.get_per_sq())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, x):
#         return self.value + int(x)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, x):
#         return len(self.value + str(x)) # Python + 35 = Python35
#
#
# t1 = Number(10)
# t2 = Text('Python')
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         return f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}'
#
#     def make_sound(self):
#         return f'{self.name} мяукает.'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         return f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}'
#
#     def make_sound(self):
#         return f'{self.name} гавкает.'
#
#
# p1 = Cat("Пушок", 2.5)
# p2 = Dog("Мухтар", 4)
#
# s = [p1, p2]
# for i in s:
#     print(i.print_info(), '\n', i.make_sound())


# class Human:
#     def __init__(self, firstname, name, age):
#         self.firstname = firstname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'\n{self.firstname}, {self.name}, {self.age}', end="")
#
#
# class Student(Human):
#     def __init__(self, firstname, name, age, special, group, rating):
#         super().__init__(firstname, name, age)
#         self.special = special
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.special}, {self.group}, {self.rating}',end="")
#
#
# class Teacher(Human):
#     def __init__(self, firstname, name, age, special, exp):
#         super().__init__(firstname, name, age)
#         self.special = special
#         self.exp = exp
#
#     def info(self):
#         super().info()
#         print(f' {self.special}, {self.exp}',end="")
#
#
# class Graduate(Student):
#     def __init__(self, firstname, name, age, special, group, rating, diplom):
#         super().__init__(firstname, name, age, special, group, rating)
#         self.diplom = diplom
#
#     def info(self):
#         super().info()
#         print(f' {self.diplom}',end='')
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#
# cat = Cat('Пушок')
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#
# p = Point(5, 7, 6)
# p2 = Point(5, 7, 6)
# print(len(p))
# print(len(p2))

# import math


# class Point:
#     __slots__ = ('x', 'y', '__length')  # запрещает создавать за пределами переменные кроме тех которые указаны в слотс
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# # pt.z = 3
# # print(pt.__dict__)
# pt.length = 10
# print(pt.x, pt.y, pt.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(10, 20)
# pt2 = Point2D(10, 20)
# print('pt=', pt.__sizeof__())
# print('pt=', pt2.__sizeof__() + pt2.__dict__.__sizeof__())
#


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt2 = Point3D(10, 20, 30)
# # pt2.z = 30
# print(pt2.x, pt2.y, pt2.z)
# # print(pt2.__dict__)


# Функторы - объекты классов которые можно выполнять как в функции(def __call__)

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
# s1 = StripChars('?:!. ')
# print(s1('Hello world!:. '))
#
#
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#     return wrap
#
#
# s2 = strip_string('?:!. ')
# print(s2('Hello world!:. '))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
# def __call__(self, *args, **kwargs):
#     print('Перед вызовом функции')
#     self.func()
#     print('После функции')

#
# @MyDecorator
# def func1():
#     print('func')
#
#
# func1()


# class MyDecorator:
#     def __init__(self, arg): #test2
#         self.name = arg
#
#     def __call__(self, func):  # add
#         def wrap(a, b):
#             print('Перед вызовом функции')
#             func(a, b)
#             print('После вызова функции')
#         return wrap
#
#
# @MyDecorator('test2')
# def add(a, b):
#     print(a, b)
#
# add(2, 5)

#
# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             res = func(a, b)
#             return res ** self.arg
#
#         return wrap
#
#
# @Power(3)
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 2))


# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#     return  wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person('Пшеничных', 'Александр')
# p1.info()


# Декорирование класса


# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))

#
# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self, value):
#         self.__value = value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)

# @property
# def name(self):
#     return self.__name
#
# @name.setter
# def name(self, value):
#     self.__name = value
#
# @property
# def surname(self):
#     return self.__surname
#
# @surname.setter
# def surname(self, value):
#     self.__surname = value


# p = Person('Ivan', 'Petrovich')
# print(p.name.get())


# Дескрипторы

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Ivan', 'Petrovich')
# print(p.name)
# print(p.surname)
#
# p.name = 'Vadim'
# print(p.name)


# DZ31

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, (int, float)) or value < 0:
#             raise ValueError(f'{self.__name} должно быть положительным числом')
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = ValidString()
#     amount = ValidString()
#
#     def __init__(self, name, price, amount):
#         self.name = name
#         self.price = price
#         self.amount = amount
#
#     def __str__(self):
#         return f'({self.name}, {self.price}, {self.amount})'
#
#
# p = Order('apple', 5, 10)
# print(p)


# Виды дескрипторов:
# non-data descriptors (дескриптор не данных) - дескрипторы, которые определили
# только __get__. Они только отдают значение, нельзя ничего сохранить. Например:
# staticmethod(), classmethod()
# data descriptor (дескриптор данных) - если объект определяет сразу и __get__,
# и __set__ и другие. Например: property()

# class ValidInt:
#     @classmethod
#     def verify_coords(cls, coord):
#         if not isinstance(coord, int):
#             raise ValueError(f"Координата {coord} должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coords(value)
#         instance.__dict__[self.name] = value
#
#
# class Point3D:
#     x = ValidInt()
#     y = ValidInt()
#     z = ValidInt()
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)


# Метаклассы
#
# a = 5
# print(type(a))
# print(type(int))

#
# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst[0] = 3
# print(lst, lst.get_length())


# type(
# имя класса
# кортеж родительских классов
# словарь, содержащий атрибуты и их значения
# )


# Создание модулей


# from geometry import sq, rect, trian
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
# s1 = sq.Square(10)
# s2 = sq.Square(20)
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())


# from car import electrocar
#
#
# def main():
#     e_car = electrocar.ElectroCar('Tesla', 'T', 2022, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     main()
#


# from shapes import rectangle, circle, cylinder
#
# circles = [circle.Circle(4), circle.Circle(5), circle.Circle(6), circle.Circle(3), circle.Circle(10), circle.Circle(8)]
# rects = [rectangle.Rectangle(10, 20),rectangle.Rectangle(4, 5), rectangle.Rectangle(16, 18), rectangle.Rectangle(1, 3), rectangle.Rectangle(15, 25)]
# cylinders = [cylinder.Cylinder(3, 4), cylinder.Cylinder(3, 9), cylinder.Cylinder(8, 4), cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5)]
#
# circle_max_s = max(circles, key=lambda i: i.get_circle_area())
# rect_min_p = min(rects, key=lambda i: i.get_rect_perimetr())
# cylinders_v = list(map(lambda i: i.get_volue(), cylinders))
# cylinder_v_avr = sum(cylinders_v) / len(cylinders_v)
# print(f'Окружность с наибольшей площадью: {circle_max_s.print_circle()} = {circle_max_s.get_circle_area()}')
# print(f'Прямоугольник с наименьшим периметром: {rect_min_p.print_rect()} = {rect_min_p.get_rect_perimetr()}')
# print(f'Средний объем всех цилиндров: {round(cylinder_v_avr, 2)}')


# Упаковка данных
# Cериализация - запись данных
# Десериализация - чтение данных

# В стандартной библиотеке Python
# marshal - модуль для поддержки (.pyc) более старой версии питон
# pickle -
# json


import pickle

# file_name = 'base.txt'
#
# shop_list = {
#     'фрукты': ['яблоки', "апельсины"],
#     'овощи': ["картошка"],
#     'бюджет': 1000
# }
#
# with open(file_name, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop_list_2 = pickle.load(fh)
#
# print(shop_list_2)


# class Test:
#     num = 35
#     str = 'Python'
#     lst = [1, 2, 3]
#     dict = {'first': 'a', 'second': 2, 'third': [1, 2, 3]}
#     tpl = (10, 20, 30)
#
#     def __str__(self):
#         return f'Число: {Test.num},\nСтрока: {Test.str}\nСписок: {Test.lst}\nСловарь: {Test.dict}\nКортеж:{Test.tpl}'
#
#
# obj = Test()
# # print(obj)
#
# d_save = pickle.dumps(obj)
# print(f'Сереализация в строку: \n{d_save}\n')
#
# d_read = pickle.loads(d_save)
# print(f'Десереализация в строку: \n{d_read}\n')


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1) # __getstate__
# item3 = pickle.loads(item2) # __setstate__
#
# print(item3.__dict__)
# print(item3)


# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.count = 0
#
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f'{self.count}: {line}'
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename)
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader('hello.txt')
# print(reader.read_line())
# print(reader.read_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.read_line())

# import json
#
# data= {
#     'first_name':'Jon',
#     'last_name':'Doe',
#     'hobbies': ('running','sky diving', 'sinding'),
#     'age': 35,
#     'children':[
#         {
#             'first_name': "Alice",
#             'age': 6,
#         },
#         {
#             'first_name': "Bob",
#             'age': 8
#         }
#     ]
# }

# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open('data_file.json', 'r') as fr:
#     data = json.load(fr)
#     print(data)


#
# json_string = json.dumps(data, sort_keys=True)
# data = json.loads(json_string)

# x = {
#     'name': "Александр"
# }
# y = {
#     'name': "Александр"
# }
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))

import json
from random import choice

# def gen_person():
#     name = ''
#     tel = ''
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#     while len(tel) != 10:
#         tel += choice(num)
#     # print(tel)
#     asdf = {
#
# print(gen_person())


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ", "
#         return f'Студент: {self.name}: {a[:-2]}'
#
#     def add_mark(self, mark):  # Метод добавления оценок
#         self.marks.append(mark)
#
#     def delete_mark(self, index):  # Метод удаления оценок
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):  # Метод замены оценок по индексу
#         self.marks[index] = new_mark
#
#     def averange_mark(self):  # Метод средне арифметическое оценок
#         return round(sum(self.marks) / len(self.marks), 2)
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + "\n"
#         return f'Группа: {self.group}\n{a}'
#
# st1 = Student('Bogdan', [5, 4, 3, 4, 5, 3])
# st2 = Student('Maksim', [5, 5, 4, 4, 5, 4])
# st3 = Student('Masha', [5, 4, 3, 4, 4, 4])
# sts = [st1, st2]
# my_group = Group(sts, 'Web-Python')
# print(my_group)
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(6)
# print(st1)
# st1.edit_mark(2, 4)
# print(st1)
# st1.averange_mark()
# print(st1.averange_mark())

import requests
import json

# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# # print(todos[:10])
# # print(type(todos))
#
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
# max_users = " and ".join(users)
# s = 's' if len(users) > 1 else ""
# print(f'user{s} {max_users} completed {max_complete} TODOs')
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo["userId"]) in users
#     return is_complete and has_max_count
#
# with open('filtered_file.json','w') as datafile:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, datafile, indent=4)
#
#
# with open('filtered_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)

import csv

# with open('CSV.csv') as r_file:
#     file_reader = csv.reader(r_file, delimiter=';')
#     count = 0
#     print(file_reader)
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         else:
#             print(f'    {row[0]} - {row[1]}. Родился в {row[2]} году.')
#         count += 1
#     print(f'Всего в файле {count} строки.')


# with open('CSV.csv') as r_file:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=';', fieldnames=field_names)
#     count = 0
#     print(file_reader)
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#             print(f'{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году.')
#         count += 1


# with open('student.csv', 'w') as fw:
#     writer = csv.writer(fw, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Саша', '5', '12'])
#     writer.writerow(['Маша', '11', '18'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
# with open('data_new.csv', 'w') as fw:
#     writer = csv.writer(fw, delimiter=',', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_new.csv') as f:
#     print(f.read())


# with open('student1.csv', 'w') as fw:
#     names = ['Имя', "Возраст"]
#     file_writer = csv.DictWriter(fw, delimiter=',', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({'Имя': "Саша", "Возраст": "15"})
#     file_writer.writerow({'Имя': "Даша", "Возраст": "25"})
#     file_writer.writerow({'Имя': "Коля", "Возраст": "5"})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict.csv", 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), delimiter=';', lineterminator='\r')
#     writer.writeheader()
#     for i in data:
#         writer.writerow(i)

