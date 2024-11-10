class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if not isinstance(other.number_of_floors, int):
            raise TypeError("Этажи должны быть целым числом")
        return self.number_of_floors == other.number_of_floors

    def __gt__(self, other):

        return self.number_of_floors > other.number_of_floors

    def __lt__(self, other):

        return self.number_of_floors < other.number_of_floors

    def __ge__(self, other):

        return self.number_of_floors >= other.number_of_floors

    def __le__(self, other):

        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):

        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            print("для арифметических операций необходимо число__add__")
        else:
            return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        if not isinstance(value, int):
            print(f"для арифметических операций необходимо число__radd__ {value} - {type(value)}")
            return self
        else:
            return self + value

    def __iadd__(self, value):
        if not isinstance(value, int):
            print("для арифметических операций необходимо число__iadd__")
            return self
        else:
            return self + value

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__