def integer_params_decorated(value):
    if value.__name__ == '__init__':
        def wrapper(s, *args):
            for i in args:
                # print(i)
                if not isinstance(i, int):
                    raise TypeError("аргументы должны быть целыми числами")
            value(s, *args)
        return wrapper
    if value.__name__ == '__setitem__':
        def wrapper(s, *args):
            if not isinstance(args[1], int):
                raise TypeError("аргументы должны быть целыми числами")
            value(s, *args)
        return wrapper
    return value

'''
решение
def integer_params_decorated(func):
    def wrapper(*args):
        if any(map(lambda x: not isinstance(x, int), args[1:])):
            raise TypeError("аргументы должны быть целыми числами")
        return func(*args)
    return wrapper
'''

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    # print(methods)
    for k, v in methods.items():
        # print(v)
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

# Vector.__getitem__.__dict__
vector = Vector(1, 2)
print(vector[1])
vector[1] = 20 # TypeError
print(vector[1])
'''
В программе объявлена функция integer_params для класса Vector, которая применяет к каждому методу класса 
декоратор integer_params_decorated:

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

Декоратор integer_params_decorated должен проверять, чтобы все передаваемые аргументы в методы класса 
(кроме первого self) были целыми числами (имели тип int). Если это не так, то должно генерироваться исключение командой:

raise TypeError("аргументы должны быть целыми числами")

Ваша задача объявить эту функцию-декоратор.

Пример использования класса (эти строчки в программе не писать):

vector = Vector(1, 2)
print(vector[1])
vector[1] = 20.4 # TypeError

P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.
'''