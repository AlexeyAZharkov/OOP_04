class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    ID = 1

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = ShopItem.ID
        ShopItem.ID += 1

    def get_id(self):
        return self.__id


item = ShopItem('name', 1, 2)
item1 = ShopItem('name', 2, 3)
print(item.get_id())
print(item1.get_id())

'''
Вам необходимо объявить класс ShopItem для представления товара в магазине. Объекты этого класса создаются командой:

item = ShopItem(name, weight, price)

где name - название товара (строка); weight - вес товара (любое положительное число); price - цена товара 
(любое положительное число).

В каждом объекте класса ShopItem должны формироваться локальные атрибуты с именами _name, _weight, _price 
и соответствующими значениями. Также в объектах класса ShopItem должен автоматически формироваться локальный 
приватный атрибут __id с уникальным (для каждого товара) целым значением.

Для считывания значения приватного атрибута __id должен быть метод:

get_id() - возвращает значение атрибута __id

Класс ShopItem должен быть объявлен так, что при отсутствии в нем метода get_id() должно генерироваться исключение командой:

raise NotImplementedError('в классе не переопределен метод get_id')

Далее следует объявить базовый класс ShopInterface (для дочернего класса ShopItem) и в этом базовом классе 
объявить метод get_id() так, чтобы генерировалось исключение NotImplementedError, если метод с тем же именем 
get_id не определен в его дочерних классах.

В классе ShopInterface не должно быть инициализатора (магического метода __init__).

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
'''