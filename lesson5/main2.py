# Пользователи:
# создайте класс с именем User Создайте два атрибута first_name и last_
# name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя
# Напишите метод describe_user(), который выводит сводку с информацией о пользователе
# Создайте еще один метод greet_user() для вывода персонального приветствия для
# пользователя
# Создайте несколько экземпляров, представляющих разных пользователей
# Вызовите оба метода для каждого пользователя
class User:
    def __init__(self, firtst_name, last_name, username, password):
        self.firtst_name = firtst_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def describe_user(self):
        return f"first name: {self.firtst_name}\nlast name: {self.last_name}\nusername: {self.username}\npassword: {self.password}\n"

    def greet_user(self):
        return f"Hi {self.firtst_name}\n"


user1 = User("Rakhim", "Aliev", "Aliev.rkh", "123123")
user2 = User("Anonim", "Anonimov", "Anonim_", "321321")

print(user2.describe_user())
print(user2.greet_user())
print(user1.describe_user())
print(user1.greet_user())


# Создайте классы Rectangle and Square с методом calculate_perimetr, вычисляющим периметр фигур, которые эти классы представляют.
# Содайте объекты Rectangle и Square вызовите в них эти методы.
# В классе Square определите метод change_size, позвляющий передавать ему число, которое увеличивает или уменьшает
# (если оно отрицательное) каждую сторону объекта Square на соответсвующее значение.
# Создайте класс Shape. Определите в нем метод what_am_i, который при вызове  выводит строку “Я фигура”.
# Измените ваши классы Rectangle и Square из предыдущих заданий для наследования от Shape, создайте объекты этих классов
# и вызовите в них новый метод.
class Rectangle:
    def calculate_perimetr(self, a, b):
        return (a + b) * 2


class Square:
    def calculate_perimetr1(self, a):
        return a * 4

    def change_size(self, increase, size):
        return (size * 4) + (increase * 4)

class Shape(Rectangle, Square):
    def what_am_i(self):
        return "Я фигура"


print(Shape().calculate_perimetr(4, 3))
print(Shape().calculate_perimetr1(3))
print(Shape().change_size(5, 4))
print(Shape().what_am_i())