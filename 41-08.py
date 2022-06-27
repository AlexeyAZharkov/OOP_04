class Singleton:
    __instance = None

    def __new__(cls, name, **kwargs):
        # print('__new__')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.name1 = name
        return cls.__instance

    def __init__(self, name):
        # print(self.name1)
        self.name = self.name1


class Game(Singleton):
    def __init__(self, name):
        super().__init__(name)

''' Верное решение '''
# class Game(Singleton):
#     def __init__(self, name):
#         if 'name' not in self.__dict__:
#             self.name = name


game = Game('name')
game1 = Game('name1')
print(id(game), id(game1))
print(game1.name)

'''
С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). Как пример, 
объявите в программе класс с именем:

Singleton

который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый). 
Как это делать, вы должны уже знать из этого курса.

Затем, объявите еще один класс с именем:

Game

который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:

game = Game(name)

где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с соответствующим содержимым.

Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так, 
то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
'''