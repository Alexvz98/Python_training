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
#         if not isinstance(key, str):
#             raise ValueError('Ключ должен быть строкой')
#         if not isinstance(value, int):
#             raise ValueError('Значение должно быть целым числом')
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3600
#         elif key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1['hour'] = 12
# c1['min'] = 20
# c1['sec'] = 30
# print(c1['hour'], c1['min'], c1['sec'])
# print(c1.get_format_time())

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


# class Point3D:
#     res = 'Координата должна быть числом'
#     reg = 'Правый операнд должен быть типом Point3D'
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f'({self.__x},{self.__y},{self.__z})'
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.reg)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.reg)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.reg)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.reg)
#         self.__check0(other) # Если отработает raise то до return не дойдет
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.reg)
#         else:
#             return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой(str)")
#         elif item == 'x':
#             return self.__x
#         elif item == 'y':
#             return self.__y
#         elif item == 'z':
#             return self.__z
#         else:
#             print('Неверно задан ключ')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой(str)")
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             elif key == 'y':
#                 self.__y = value
#             elif key == 'z':
#                 self.__z = value
#             else:
#                 print('Заданны некоректные данные')
#
#     @staticmethod
#     def __check0(exem):
#         if exem.x == 0 or exem.y == 0 or exem.z == 0:
#             raise ZeroDivisionError('Ни одна из координат не должна равняться 0')
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.res)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.res)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.res)
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print('Координаты 1-ой точки: ', pt1)
# print('Координаты 2-ой точки: ', pt2)
#
# pt3 = pt1 + pt2
# print(f"Сложение координат: {pt3}")
#
# pt4 = pt1 - pt2
# print(f'Вычитание координат: {pt4}')
#
# pt5 = pt1 * pt2
# print(f'Умножение координат: {pt5}')
#
# pt6 = pt1 / pt2
# print(f'Деление координат: {pt6}')
#
# pt7 = pt1 == pt2
# print(f'Равенство: {pt7}')
#
# print('x =', pt1['x'], 'x1 =', pt2['x'])
# print('y =', pt1['y'], 'y1 =', pt2['y'])
# print('z =', pt1['z'], 'z1 =', pt2['z'])
#
# pt1['x'] = 20
# print('Запись значения в координату x:', pt1['x'])