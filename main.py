# Git & ООП

# Инкапсуляция (encapsulation) - техника, при которой несущественная с точки
# зрения интерфейса объекта информация прячется внутри него.

# Наследование (inheritance) - свойство объектов, посредством которого экземпляры
# класса получают доступ к данным и методам классов-предков без их повторного
# определения.

# Полиморфизм (polymorphism) -  свойство, позволяющее использовать один и тот же
# интерфейс для различных действий.


class Vehicle(object):
    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed
        print('Было создано транспортное средство')

    def accelerate(self,x):
        self.speed = self.speed + x
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self,x):
        self.speed = self.speed - x
        if self.speed < 0:
            self.speed = 0

    def print_status(self):
        print('Скорость транспортного средства равна {0} км/ч'.format(self.speed))
