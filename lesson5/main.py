# Определите класс Appple с четыремя переменными экземпляра, представляющими четыре свойства яблока.
class Apple:
    def __init__(self, size, color, juiciness, cricle):
        self.size = size
        self.color = color
        self.juiciness = juiciness
        self.cricle = cricle


# Создайте класс Circle с методом area, подсчитывающими и возвращающим площадь круга. Затем создайте объект Circle, вызовите в нем метод area и выведите результат.
# Воспользуйтесь функцией Pi из встроенного в python модуля math.
import math
class Cricle:
    def area(self, radius):
        return math.pi * radius


cricle = Cricle()
print(cricle.area(50))


# Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника. Затем создайте объект этого класса, вызовите в нем area и выведите результат.
class Triangle:
    def area(self, a, b):
        return a * b / 2

triangle = Triangle()
print(triangle.area(1, 1))


# Создайте класс Hexagon с методом calculate_perimetr, подсчитывающим и возвращающим периметр шестиугольника. Затем создайте объект Hexagon, вызовите в нем calculate_perimetr и выведите результат.
class Hexagon:

    def calculate_perimetr(self, side):
        return side * 6

hexagon = Hexagon()
print(hexagon.calculate_perimetr(5))


# Ресторан:
# создайте класс с именем Restaurant Метод init() класса Restaurant должен содержать два атрибута: restaurant_name и cuisine_type
# Создайте метод describe_
# restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит
# сообщение о том, что ресторан открыт
# Создайте на основе своего класса экземпляр с именем restaurant Выведите два атрибута по отдельности, затем вызовите оба метода
# Три ресторана:
# Создайте три разных экземпляра, вызовите для каждого экземпляра метод describe_restaurant()
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe(self):
        return f"Имя ресторана: {self.restaurant_name}\nТип кухни: {self.cuisine_type}"

    def open_restaurant(self):
        return f"Ресторан {self.restaurant_name} открыт"


restaurant = Restaurant("Benefis", "fast food")
restaurant1 = Restaurant("Fast", "food")
restaurant2 = Restaurant("Food", "fast")
print(restaurant.describe() + "\n")
print(restaurant1.describe() + "\n")
print(restaurant2.describe() + "\n")
print(restaurant.open_restaurant() + "\n")


