class Figure:

    def __init__(self, *args):
        self.args = args
        self.__color = args[0]
        self.ides_count = 0
        self.__sides = None
        self.__color = []
        self.filled = True

    def get_color(self):
        return self.__color

    def get_sides(self):
        self.__sides = self.args[1]
        return self.__sides

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = list((r, g, b))
        else:
            self.__color = list(self.args[0])

    def __is_valid_sides(self, sides_count):
        self.args = list(self.args)
        try:
            check = sum([1 for i in range(1, len(self.args)) if self.args[i] > 0])
            if check == sides_count:
                return True
            else:
                return False
        except:
            check = sum([1 for i in range(1, len(self.args[1])) if self.args[i] > 0])
            if check == sides_count:
                return True
            else:
                return False

    def get_is_valid_sides(self, sides_count):
        return self.__is_valid_sides(sides_count)

    def change_figure(self, sides_count):
        if self.get_is_valid_sides(sides_count):
            self.args = list(self.args)
        else:
            self.args = list(self.args)
            self.args[1] = [self.args[1]] * sides_count

    def set_sides(self, *args1):
        args1 = list(args1)
        if len(list(self.args[1:])) == len(args1):
            self.args = list(self.args)
            self.args[1] = [i for i in args1]


class Circle(Figure):
    sides_count = 1
    __radius = 0

    def __len__(self):
        try:
            return self.args[1][0] * self.sides_count
        except:
            return self.args[1] * self.sides_count

    def get_radius(self):
        self.__radius = self.args[1]
        return self.__radius

    def change_Circle(self):
        return self.change_figure(self.sides_count)


class Triangle(Figure):
    sides_count = 3

    def __init__(self):
        self.__height = None

    def set_height(self):
        self.args = list(self.args)
        try:
            p = sum([self.args[i] for i in range(1, len(self.args)) if self.args[i] > 0])
            s = (p * (p - self.args[0]) * (p - self.args[1]) * (p - self.args[1])) ** 0.5
            h = 2 * s / self.args[0]
            return h
        except:
            p = sum([self.args[i] for i in range(1, len(self.args)) if self.args[i] > 0])
            s = (p * (p - self.args[1][0]) * (p - self.args[1][1]) * (p - self.args[1][2])) ** 0.5
            h = 2 * s / self.args[0]
            return h

    def set_height(self):
        self.__height = Triangle.set_height
        return self.__height

    def get_square(self):
        try:
            p = sum([self.args[i] for i in range(1, len(self.args)) if self.args[i] > 0])
            s = (p * (p - self.args[0]) * (p - self.args[1]) * (p - self.args[1])) ** 0.5
        except:
            p = sum([self.args[i] for i in range(1, len(self.args)) if self.args[i] > 0])
            s = (p * (p - self.args[1][0]) * (p - self.args[1][1]) * (p - self.args[1][2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        try:
            return self.args[1][1] ** 3
        except:
            return self.args[1] ** 3

    def __len__(self):
        try:
            return self.args[1][0] * self.sides_count
        except:
            return self.args[1] * self.sides_count

    def change_cube(self):
        return self.change_figure(self.sides_count)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
circle1.change_Circle()
cube1 = Cube((222, 35, 130), 6)
cube1.change_cube()
# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
circle1.change_Circle()
print(*circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
# Проверка объёма (куба):
print(cube1.get_volume())
