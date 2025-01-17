class House:
    houses_history = []
    def  __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
            return
        for i in range(1, new_floor + 1):
            print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнение возможно только с объектами типа House")
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнение возможно только с объектами типа House")
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнение возможно только с объектами типа House")
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнение возможно только с объектами типа House")
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнение возможно только с объектами типа House")
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнение возможно только с объектами типа House")
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно добавлять только целые числа")
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно вычитать только целые числа")
        self.number_of_floors -= value
        return self

    def __rsub__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно вычитать только целые числа")
        self.number_of_floors = value - self.number_of_floors
        return self

    def __isub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно умножать только на целые числа")
        self.number_of_floors *= value
        return self

    def __rmul__(self, value):
        return self.__mul__(value)

    def __imul__(self, value):
        return self.__mul__(value)

    def __floordiv__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно делить только на целые числа")
        if value == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        self.number_of_floors //= value
        return self

    def __rfloordiv__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно делить только на целые числа")
        if self.number_of_floors == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        self.number_of_floors = value // self.number_of_floors
        return self

    def __ifloordiv__(self, value):
        return self.__floordiv__(value)

    def __mod__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно вычислять остаток только для целых чисел")
        self.number_of_floors %= value
        return self

    def __rmod__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно вычислять остаток только для целых чисел")
        self.number_of_floors = value % self.number_of_floors
        return self

    def __imod__(self, value):
        return self.__mod__(value)

    def __pow__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно возводить в степень только целые числа")
        self.number_of_floors **= value
        return self

    def __rpow__(self, value):
        if not isinstance(value, int):
            raise TypeError("Можно возводить в степень только целые числа")
        self.number_of_floors = value ** self.number_of_floors
        return self

    def __ipow__(self, value):
        return self.__pow__(value)

if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)

    print(House.houses_history)

    h2 = House('ЖК Акация', 20)

    print(House.houses_history)

    h3 = House('ЖК Матрёшки', 20)

    print(House.houses_history)

    # Удаление объектов

    del h2

    del h3

    print(House.houses_history)