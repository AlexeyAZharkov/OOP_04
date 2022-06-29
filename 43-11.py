class ItemAttrs:
    def __getitem__(self, item):
        # tup = tuple(*self.__dict__.values())
        # print(tup)
        # print(tup[item])
        return tuple(*self.__dict__.values())[item]

    def __setitem__(self, key, value):
        tup = tuple(*self.__dict__.items())
        print(tup)


class Point(ItemAttrs):
    def __init__(self, *args):
        self.coord = args


pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
print(x, y)
pt[0] = 10

'''
Объявите базовый класс с именем ItemAttrs, который бы позволял обращаться к локальным атрибутам объектов 
дочерних классов по индексу. Для этого в классе ItemAttrs нужно переопределить следующие методы:

__getitem__() - для получения значения атрибута по индексу;
__setitem__() - для изменения значения атрибута по индексу.

Объявите дочерний класс Point для представления координаты точки на плоскости. Объекты этого класса должны создаваться командой:

pt = Point(x, y)

где x, y - целые или вещественные числа.

Пример использования классов (эти строчки в программе не писать):

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10

P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
'''