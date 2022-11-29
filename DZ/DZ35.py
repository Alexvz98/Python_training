# import json
#
# data = {'Россия': 'Москва'}
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f'{self.country}: {self.capital}'
#
#     @classmethod
#     def add_country(cls, new_country, new_capital, file_name):
#         try:
#             data1 = json.load(open(file_name))
#         except FileNotFoundError:
#             data1 = {}
#
#         data1[new_country] = new_capital
#
#         with open(file_name, 'w') as f:
#             json.dump(data1, f, indent=2, ensure_ascii=False)
#
#     @classmethod
#     def delete_country(cls, del_country, file_name):
#         try:
#             data1 = json.load(open(file_name))
#         except FileNotFoundError:
#             data1 = {}
#         if del_country in data1:
#             del data1[del_country]
#             with open(file_name, 'w') as f:
#                 json.dump(data1, f, indent=2, ensure_ascii=False)
#         else:
#             print(f'Страны {del_country} нет в базе данных')
#     @classmethod
#     def search_data(cls, country_name, file_name):
#         try:
#             data1 = json.load(open(file_name))
#         except FileNotFoundError:
#             data1 = {}
#
#         if country_name in data1:
#             print(f'Страна {country_name} столица {data1[country_name]} есть в словаре!')
#         else:
#             print(f'{country_name} отсутствует в словаре!')
#
#     @classmethod
#     def change_capital(cls, country_name, new_capital, file_name):
#         try:
#             data1 = json.load(open(file_name))
#         except FileNotFoundError:
#             data1 = {}
#         if country_name in data:
#             data1[country_name] = new_capital
#             with open(file_name, 'w') as f:
#                 json.dump(data1, f, indent=2, ensure_ascii=False)
#         else:
#             print(f'Страны {country_name} не существует в базе данных')
#
#
#
#     @classmethod
#     def load_from_file(cls, file_name):
#         with open(file_name, 'r') as f:
#             print(json.load(f))
#
#
# index = ''
# file_name1 = 'list_capital.json'
# with open(file_name1, 'w') as fw:
#     json.dump(data, f, indent=2, ensure_ascii=False)
#
# while index != 6:
#     try:
#         print('*' * 40)
#         index = int(input('Выбор действия:\n'
#                           '1 - добавление данных\n'
#                           '2 - удаление данных\n'
#                           '3 - поиск данных\n'
#                           '4 - редактор данных\n'
#                           '5 - просмотр данных\n'
#                           '6 - завершение работы\n'
#                           'Ввод: '))
#         if index == 1:
#             country_name = input('Введите название страны (с заглавной буквы): ')
#             capital_name = input('Введите название столицы страны (с заглавной буквы): ')
#             CountryCapital.add_country(country_name, capital_name, 'list_capital.json')
#             print('Файл сохранен')
#
#         if index == 2:
#             country_name = input('Введите страну для удаления: ')
#             CountryCapital.delete_country(country_name, 'list_capital.json')
#             print('Файл сохранен')
#
#         if index == 3:
#             country_name = input('Введите страну для поиска: ')
#             CountryCapital.search_data(country_name, 'list_capital.json')
#             print('Файл сохранен')
#
#         if index == 4:
#             country_name = input('Введите страну для редактирования столицы: ')
#             new_capital = input('Введите новое название столицы: ')
#             CountryCapital.change_capital(country_name, new_capital, 'list_capital.json')
#             print('Файл сохранен')
#
#         if index == 5:
#             CountryCapital.load_from_file('list_capital.json')
#
#     except IndexError:
#         break
