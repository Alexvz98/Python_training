# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# class Parser:
#     html = ""
#     res = []
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         news = self.html.find_all('article')
#         for item in news:
#             title = item.find('h3', class_="promo__heading").text.strip()
#             href = item.find('a').get('href')
#             self.res.append({
#                 'title': title,
#                 'href': href
#             })
#         print(self.res)
#
#     def save(self):
#         with open(self.path, 'w') as f:
#             i = 1
#             for item in self.res:
#                 f.write(f"Акция № {i}\n\n Название: {item['title']}\n"
#                         f" Ссылка: {item['href']}"
#                         f"\n\n{'*' * 40}\n")
#                 i += 1
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#         self.save()
