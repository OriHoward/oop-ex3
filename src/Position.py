class Position:

    def __init__(self, x=0, y=0, z=0):
        self._x: float = float(x)
        self._y: float = float(y)
        self._z: float = float(z)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z
