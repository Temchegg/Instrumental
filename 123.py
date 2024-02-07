# import random
#
#
# class MusicAlbum:
#
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def print_all(self):
#         print(f'Название: {self.title}\n'
#               f'Исполнитель: {self.artist}\n'
#               f'Год: {self.release_year}\n'
#               f'Жанр: {self.genre}\n'
#               f'Треки: {self.tracklist}')
#
#     def play_random_track(self):
#         num = random.randint(0, len(self.tracklist))
#         track_rand = self.tracklist[num]
#         print(f'Воспроизводится трек {num + 1}: {track_rand}')
#
#
#
# tracklist = ['Deutschland', 'Radio', 'Zeigdich', 'Auslander', 'Sex', 'Puppe', 'Wasichliebe', 'Diamant', 'Weitweg', 'Tattoo', 'Hallomann']
# rammstein = MusicAlbum('Deutschland', 'Rammstein', 2019, 'Neue Deutsche Harte', tracklist)
# rammstein.print_all()
# rammstein.play_random_track()
#
# from statistics import mean
#
#
# class Student:
#     def __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def print_all(self):
#         print(f'Имя: {self.name}\n'
#               f'Возраст: {self.age}\n'
#               f'Класс: {self.grade}\n'
#               f'Оценки: {self.scores}')
#
#     def average_score(self):
#         avg_score = mean(self.scores)
#         print(f'Средний балл: {avg_score}')
#
# egor = Student("Егор Данилов", "12", "5В", [5, 4, 4, 5])
# egor.print_all()
# egor.average_score()
#
# class Recipe:
#
#     def __init__(self, name, recipe):
#         self.name = name
#         self.recipe = recipe
#
#     def print_ingredients(self):
#         print(f'Ингридиенты для {self.name}:')
#         for i in range (len(self.recipe)):
#             print(f'- {self.recipe[i]}')
#
#     def cook(self):
#         print(f'Выполняем инструкцию по приготовлению блюда {self.name}...\n'
#               f'Блюдо {self.name} готово!')
#
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
# spaghetti.print_ingredients()
# spaghetti.cook()
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
# cake.print_ingredients()
# cake.cook()
