class Coordinate:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return float(self._x)

    @x.setter
    def x(self, value_1):
        if not isinstance(value_1, (int, float)):
            raise TypeError("the value must be a float type.")

        self._x = value_1

    @property
    def y(self):
        return float(self._y)

    @y.setter
    def y(self, value_2):
        if not isinstance(value_2, (int, float)):
            raise TypeError("the value must be a `float` type.")

        self._y = value_2

    def distance_to_origin(self):
        return (self._x**2+self._y**2)**(1/2)

    def __add__(self, other):
        add_1 = self._x+other.x
        add_2 = self._y+other.y
        return (Coordinate(add_1, add_2))

    def __sub__(self, other):
        sub_1 = self._x-other.x
        sub_2 = self._y-other.y
        return (Coordinate(sub_1, sub_2))

Coordinate(1,2) + Coordinate(2,3)