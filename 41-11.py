class Vector:
    def __init__(self, *args):
        self.vect_lst = list(args)
        print(self.vect_lst)

    def __add__(self, other):
        self.check(other)
        res = [self.vect_lst[i] + other.vect_lst[i] for i in range(len(self.vect_lst))]
        for r in res:
            if isinstance(r, float):
                return Vector(*res)
        return VectorInt(*res)

    def __sub__(self, other):
        self.check(other)
        res = [self.vect_lst[i] - other.vect_lst[i] for i in range(len(self.vect_lst))]
        for r in res:
            if isinstance(r, float):
                return Vector(*res)
        return VectorInt(*res)

    def get_coords(self):
        return tuple(self.vect_lst)

    def check(self, other):
        if len(self.vect_lst) != len(other.vect_lst):
            raise TypeError('размерности векторов не совпадают')

    def __str__(self):
        return ' '.join(str(i) for i in self.vect_lst)


class VectorInt(Vector):
    def __init__(self, *args):
        if any(not isinstance(i, int) for i in args):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)


v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 2, 3, 4)

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5.0)
v = v1 + v2 # формируется новый вектор с соответствующими координатами
print(v.get_coords(), '  v ', type(v))
v3 = v1 - v2 # формируется новый вектор с соответствующими координатами
print(v3.get_coords(), '  v3 ', type(v3))
'''
Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)

где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор с соответствующими координатами
v = v1 - v2 # формируется новый вектор с соответствующими координатами

Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')

В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')

При операциях сложения и вычитания:

v = v1 + v2
v = v1 - v2

должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. 
Иначе, v должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
'''