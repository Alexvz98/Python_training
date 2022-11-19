# class Book:
#     name = 'Название книги'
#     age_v = 'Год выпуска'
#     avtor = 'Имя автора'
#     genre = 'Жанр'
#     price = 'Цена'
#
#     def print_info(self):
#         print('Книжная лавка'.center(40, '-'))
#         print(f'Название книги: {self.name}\n'
#               f'Год выпуска: {self.age_v}\n'
#               f'Имя автора: {self.avtor}\n'
#               f'Жанр: {self.genre}\n'
#               f'Цена: {self.price}')
#
#     def input_info(self, name, age_v, avtor, genre, price):
#         self.name = name
#         self.age_v = age_v
#         self.avtor = avtor
#         self.genre = genre
#         self.price = price
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_age_v(self, age_v):
#         self.age_v = age_v
#
#     def get_age_v(self):
#         return self.age_v
#
#     def set_avtor(self, avtor):
#         self.avtor = avtor
#
#     def get_avtor(self):
#         return self.avtor
#
#     def set_genre(self, genre):
#         self.genre = genre
#
#     def get_genre(self):
#         return self.genre
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# p1 = Book()
# p1.print_info()
# p1.input_info('Мастер и Маргарита', '1928', 'Булгаков М.А.', 'Роман', '460 рублей')
# p1.print_info()
# print()
# p1.set_name('Война и мир')
# p1.set_age_v('1865 г.')
# p1.set_avtor('Толстой А.А.')
# p1.set_genre('Роман')
# p1.set_price('600 рублей')
# print(p1.get_name())
# print(p1.get_age_v())
# print(p1.get_avtor())
# print(p1.get_genre())
# print(p1.get_price())
# p1.print_info()
