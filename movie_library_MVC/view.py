def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f' {title} '.center(50, '='))
            output = func(*args, **kwargs)
            print('=' * 50)
            return output

        return wrap

    return wrapper


class UserInterface():

    @add_title('Редактирование данных каталога фильмов')
    def wait_user_answer(self):
        print('Действие с фильмами: ')
        print('1 - добавление фильма\n'
              '2 - каталог фильмов\n'
              '3 - просмотр определенного фильма\n'
              '4 - удаление фильма\n'
              'q - выход из программы')
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    def add_movie(self):
        dict_movie = {
            'название фильма': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': None
        }
        for key in dict_movie:
            dict_movie[key] = input(f'Введите {key} фильма: ')
        return dict_movie

    @add_title(" Список фильмов ")
    def show_all_movies(self, movies):
        for ind, movie in enumerate(movies, start=1):
            print(f'{ind}. {movie}')

    @add_title(' Ввод названия статьи ')
    def get_user_movie(self):
        user_movie = input('Введите название фильма: ')
        return user_movie

    @add_title(' Просмотр фильма ')
    def show_single_movie(self, movie):
        for key in movie:
            print(f'{key} фильм - {movie[key]}')

    @add_title(' Сообщение об ошибке ')
    def show_incorrect_title_error(self, user_title):
        print(f'Фильма с названием {user_title} не существует.')

    @add_title('Удаление фильма')
    def remove_single_movie(self, movie):
        print(f'Фильм {movie} - был удален')