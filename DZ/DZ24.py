# class Point:
#
#     def __init__(self, kg=0):
#         self.__kg = kg
#
#     @property
#     def pr_kg(self):
#         return self.__kg
#
#     @pr_kg.setter
#     def pr_kg(self, kg):
#         self.__kg = kg
#
#     @classmethod
#     def results(cls, kg):
#         if isinstance(kg, int) or isinstance(kg, float):
#             kg = kg * 2.205
#             return kg
#         else:
#             return "Введены некорректные данные"
#
#
# a = 12
# b = 41
# c = "abc"
# p1 = Point.results(a)
# p2 = Point.results(b)
# p3 = Point.results(c)
# print(a, 'кг =>', p1, 'фунтов')
# print(b, 'кг =>', p2, 'фунтов')
# print(c, 'кг =>', p3, 'фунтов')
#
