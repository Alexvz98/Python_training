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
#     def sum(self):
#         return self.price * self.amount
#
#
# p = Order('apple', 5, 10)
# print(p)
# print(p.sum())