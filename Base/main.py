# --- List , Dict , Set , Generator Comprehension == Генераторы Списком , Множеств, Словарей , Генераторов

my_list = [a for a in range(10) if a % 2 == 0]
my_set = {a for a in range(10) if a % 2 == 0}
my_dict = {a: 10 for a in range(10) if a % 2 == 0}
my_generator = (a for a in range(10) if a % 2 == 0)


# -----   Области Видимости Переменной , LEGB (Local, Enclosing, Global and Built-in)   -----------------------------------------------------------------------------------------------------------------------

str = "global"


def outer():
    str = "Enclosing"

    def inner():
        str = "local"
        print(str)

    print(str)
    inner()


# --- global позвоялет использовате переменную из глобальной области видимости

a = 3
# a = 3 -> a = 5


def outer():
    global a
    a = 5


outer()


# --- nonlocal позволяет использовать переменую, которая лежит во внешней функции


def outer():
    a = 3

    def inner():
        nonlocal a
        a = 5

    inner()
    # print(a)   a = 3 -> a = 5


# -----   Итераторы и Итерируемые Обьекты   ------------------------------------------------------------------------------------------------------------
# итератор имеет методы iter и next
# итерируемый обьект имеет только метод iter

a = [1, 2, 3, 4, 5]


# возвращает итератор итерируемого обьекта
iter(a)
a.__iter__()


# проходимся по елементам итерируемого обьекта
b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))


# класс, который поддерживает протокол итератора
class Counter:
    current: int

    def __init__(self):
        self.current = 0

    def __iter__(self):
        # возвращаем сам итератор
        return self

    def __next__(self):
        current = self.current
        self.current += 1
        return current


c = Counter()
# for i in c:
#     print(i)

# -----   Генераторы   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# генератор - последовательность, которая возвращает функцию


def my_fn():
    my_list = [1, 2, 3, 4, 5]
    yield my_list


for i in my_fn():
    # print(i)
    pass


# --- можно использовать много yield
def my_fn2():
    yield 1
    yield 2
    yield 3


a = my_fn2()
# next проходиться по каждому yield нашей функции my_fn2
next(a)
next(a)
next(a)


# --- yield form позволяет брать все значения возвращаемого генератора из другой функции
def first():
    yield 1
    yield 1


def second():
    yield from first()
    yield 2
    yield 2


a = second
# a -> 1 , 1 , 2 , 2


# -----   Менеджеры Контекста , конструкция with   ----------------------------------------------------------------------------------------------------------------------------------------------------
# позволяет работать при доступе к ресурсу (базе данных , файлам , сесии на сайте )
# менеджер контекста автоматически закрывают подключение к ресурсу и позволяет обрабатывает искулючения которые возникли внутри его


# with open("my_file.txt", "w") as file:
#     file.write("111")


# пример без менеджера контекста
# file = open("my_file.txt", "w")
# file.write("123")
# file.close()


# -----   КОПИИ   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# --- Поверхносная Копия
# две переменные сылаються на один обьект в памяти
a = [1, [1]]
b = a
b.append(2)
# a = [1,[1],2]
# b = [1,[1],2]

# Другие Примеры
b = list(a)
b = a[:]
b = [i for i in range(10)]

# --- Глубокая Копия
# копируються только елементы первой вложености списка
# текущая переменая всеравно ссылаеться на внутренние списки предидущей переменной

import copy

a = [1, [1]]
b = copy.copy(a)
b[1].append(2)
# a = [1,[1,2]
# b = [1,[1,2]

# --- Очень Глубокая Копия
# копируються все елементы переменной, даже вложенные
import copy

a = [1, [1]]
b = copy.deepcopy(a)
b[1].append(2)
# a = [1,[1]]
# b = [1,[1,2]]
