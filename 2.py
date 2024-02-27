# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#
#
# point = Point(3, 5)
# print(point.x, point.y)

# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#
#     def move(self, new_x, new_y):
#         self.x += new_x
#         self.y += new_y
#
#     def length(self, point2):
#         result = ((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2) ** 0.5
#         return round(result, 2)
#
#
# point = Point(3, 5)
# print(point.x, point.y)
# point.move(2, -3)
# print(point.x, point.y)

# class RedButton:
#     def __init__(self) -> None:
#         self.counter = 0
#
#     def click(self):
#         self.counter += 1
#         print('Тревога!')
#
#     def count(self):
#         return self.counter
#
#
# first_button = RedButton()
# second_button = RedButton()
# for time in range(5):
#     if time % 2 == 0:
#         second_button.click()
#     else:
#         first_button.click()
# print(first_button.count(), second_button.count())

# class Programmer:
#     __rank = {
#         'Junior': 10,
#         'Middle': 15,
#         'Senior': 20,
#     }
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.bonus = 0
#         self.work_time = 0
#         self.salary = 0
#
#     def work(self, time):
#         self.work_time += time
#         self.salary += (self.__rank[self.position] + self.bonus) * time
#
#     def info(self):
#         return f'{self.name} {self.work_time}ч. {self.salary}тгр.'
#
#     def rise(self):
#         match self.position:
#             case 'Junior':
#                 self.position = 'Middle'
#             case 'Middle':
#                 self.position = 'Senior'
#             case 'Senior':
#                 self.bonus += 1
#
#
# programmer = Programmer('Васильев Иван', 'Junior')
# programmer.work(750)
# print(programmer.info())
# programmer.rise()
# programmer.work(500)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())

# class Rectangle:
#     def __init__(self, *coords):
#         self.coords = coords
#         self.width = abs(self.coords[0][0] - self.coords[1][0])
#         self.height = abs(self.coords[0][1] - self.coords[1][1])
#
#     def perimeter(self):
#         return round(2 * (self.width + self.height), 2)
#
#     def area(self):
#         return round(self.width * self.height, 2)
#
#
# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.perimeter())

# class Rectangle:
#     def __init__(self, corner1, corner2) -> None:
#         self.left_down = [min(corner1[0], corner2[0]),
#                           min(corner1[1], corner2[1])]
#         self.up_right = [max(corner1[0], corner2[0]),
#                          max(corner1[1], corner2[1])]
#
#     def perimeter(self):
#         return round((self.up_right[0] - self.left_down[0]) * 2 +
#                      (self.up_right[1] - self.left_down[1]) * 2, 2)
#
#     def area(self):
#         return round((self.up_right[0] - self.left_down[0]) *
#                      (self.up_right[1] - self.left_down[1]), 2)
#
#     def get_pos(self):
#         return round(self.left_down[0], 2), round(self.up_right[1], 2)
#
#     def get_size(self):
#         return round(self.up_right[0] - self.left_down[0], 2), \
#             round(self.up_right[1] - self.left_down[1], 2)
#
#     def move(self, dx, dy):
#         self.left_down[0] += dx
#         self.left_down[1] += dy
#         self.up_right[0] += dx
#         self.up_right[1] += dy
#
#     def resize(self, width, height):
#         self.up_right[0] = self.left_down[0] + width
#         self.left_down[1] = self.up_right[1] - height
#
# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.get_pos(), rect.get_size())
# rect.move(1.32, -5)
# print(rect.get_pos(), rect.get_size())

# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = round(x, 2)
#         self.y = round(y, 2)
#
#     def round(self):
#         self.x = round(self.x, 2)
#         self.y = round(self.y, 2)
#         return self
#
#
# class Rectangle:
#     def __init__(self, corner1, corner2) -> None:
#         self.corner = Point(min(corner1[0], corner2[0]), max(corner1[1], corner2[1]))  # noqa
#         self.width = round(max(corner1[0], corner2[0]) - self.corner.x, 2)
#         self.height = round(self.corner.y - min(corner1[1], corner2[1]), 2)
#
#     def perimeter(self):
#         return round((self.width + self.height) * 2, 2)
#
#     def area(self):
#         return round(self.width * self.height, 2)
#
#     def get_pos(self):
#         return self.corner.x, self.corner.y
#
#     def get_size(self):
#         return self.width, self.height
#
#     def move(self, dx, dy):
#         self.corner.x += dx
#         self.corner.y += dy
#         self.corner.round()
#
#     def resize(self, width, height):
#         self.width = round(width, 2)
#         self.height = round(height, 2)
#
#     def turn(self):
#         delta = round((self.width - self.height) / 2, 2)
#         self.move(delta, delta)
#         self.height, self.width = self.width, self.height
#
#     def scale(self, ratio):
#         dx = round((self.width * (ratio - 1)), 2)
#         dy = round((self.height * (ratio - 1)), 2)
#         self.move(-dx / 2, dy / 2)
#         self.resize(self.width * ratio, self.height * ratio)
#
#
# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.scale(2.0)
# print(rect.get_pos(), rect.get_size(), sep='\n')

# class Queue:
#     queue = []
#
#     def push(self, item):
#         self.queue.append(item)
#
#     def pop(self):
#         return self.queue.pop(0)
#
#     def is_empty(self):
#         return self.queue == []
#
#
# queue = Queue()
# for item in range(10):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop(), end=" ")

# class Stack:
#     def __init__(self) -> None:
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         return self.stack.pop()
#
#     def is_empty(self):
#         return self.stack == []
#
#
# stack = Stack()
# for item in range(10):
#     stack.push(item)
# while not stack.is_empty():
#     print(stack.pop(), end=" ")