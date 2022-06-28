class ListInteger(list):
    def __init__(self, tup):
        self.check(*tup)
        super().__init__(tup)

    def __setitem__(self, item, value):
        self.check(value)
        super().__setitem__(item, value)

    def append(self, value):
        self.check(value)
        super().append(value)

    def check(self, *args):
        if not all(isinstance(i, int) for i in args):
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger((1, 2, 3, 1))
s[1] = 10
print(s[1])
s.append(11)
print(s)
# s[0] = 10.5 # TypeError

'''
Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится задача создать 
класс с именем ListInteger с базовым классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только из целые числа. При попытке присвоить любой другой тип данных, 
генерировать исключение командой:

raise TypeError('можно передавать только целочисленные значения')

Пример использования класса ListInteger (эти строчки в программе не писать):

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError

P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.
'''