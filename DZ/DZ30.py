# import math
# from abc import ABC, abstractmethod
#
#
# class Share(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def square(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#
# class Square(Share):
#     def __init__(self, w, color):
#         self.w = w
#         super().__init__(color)
#
#     def perimeter(self):
#         perimeter = self.w * 4
#         return perimeter
#
#     def square(self):
#         return self.w * self.w
#
#     def draw(self):
#         print(('*' * self.w + '\n') * self.w)
#
#     def info(self):
#         print(f'===Квадрат===\nСторона:{self.w}\nЦвет:{self.color}\nПлощадь:{s.square()}\nПериметр:{s.perimeter()}')
#
#
# class Rectangle(Share):
#     def __init__(self, w, h, color):
#         self.w = w
#         self.h = h
#         super().__init__(color)
#
#     def perimeter(self):
#         perimeter = self.w * 2 + self.h * 2
#         return perimeter
#
#     def square(self):
#         return self.w * self.h
#
#     def draw(self):
#         print(('*' * self.h + '\n') * self.w)
#
#     def info(self):
#         print(f'===Прямоугольник===\nСторона 1:{self.w}\nСторона 2:{self.h}\nЦвет:{self.color}\nПлощадь:{s.square()}\nПериметр:{s.perimeter()}')
#
#
# class Triangle(Share):
#     def __init__(self, w, h, l, color):
#         self.w = w
#         self.h = h
#         self.l = l
#         super().__init__(color)
#
#     def perimeter(self):
#         perimeter = (self.w + self.h + self.l) / 2
#         return perimeter
#
#     def square(self):
#         return self.w / 4 * math.sqrt(4 * self.h ** 2 - self.w ** 2)
#
#     def draw(self):
#         rows = []
#         for i in range(self.h):
#             rows.append(' ' * i + '*' * (self.w - 2 * i) + ' ' * i)
#         print('\n'.join(reversed(rows)))
#
#     def info(self):
#         print(
#             f'===Треугольник===\nСторона 1:{self.w}\nСторона 2:{self.h}\nСторона 3:{self.l}\nЦвет:{self.color}\nПлощадь:{s.square()}\nПериметр:{s.perimeter()}')
#
#
# s = Square(3, 'red')
# s.info()
# s.draw()
# r = Rectangle(3, 7,'yellow')
# r.info()
# r.draw()
# t = Triangle(11, 6, 6, 'green')
# t.info()
# t.draw()
