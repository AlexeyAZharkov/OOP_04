class IteratorAttrs:
    def __iter__(self):
        self.id = 0
        return self

    def __next__(self):
        ls = list(self.__dict__)
        res = ls[self.id], self.__dict__[ls[self.id]]
        if self.id < len(self.__dict__) - 1:
            self.id += 1
        else:
            raise StopIteration
        return res


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('model', (22, 33), 2222)
for attr, value in phone:
    print(attr, value)

'''
Объявите в программе базовый класс с именем IteratorAttrs для перебора всех локальных атрибутов объектов класса. 
В этом классе нужно определить два метода:

__iter__() - для получения объекта-итератора (в данном случае - это сам объект self)
__next__() - для перебора локальных атрибутов объекта self (используйте для этого словарь __dict__)

Метод __next__() на каждой итерации должен возвращать кортеж в формате: (имя атрибута, значение).

Объявите дочерний класс SmartPhone, объекты которого создаются командой:

phone = SmartPhone(model, size, memory)

где model - модель смартфона (строка); size - габариты (ширина, длина) в виде кортежа двух чисел; memory - 
размер ОЗУ (памяти), как целое число. В каждом объекте класса SmartPhone должны создаваться соответствующие 
локальные атрибуты: model, size, memory.

Благодаря наследованию от базового класса IteratorAttrs, с объектами класса SmartPhone должен выполняться оператор for:

for attr, value in phone:
    print(attr, value)

P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
'''