from dataclasses import dataclass
# import numpy as np
# import numba


@dataclass
class Coordinate:
    x: float
    y: float
    z: float


@dataclass
class CoordinateSystem:
    ox: Coordinate
    oy: Coordinate
    oz: Coordinate


class Dot:
    def __init__(self, number: int,
                 orthogonal_coordinate: Coordinate,
                 new_coordinate_system: CoordinateSystem,
                 new_coordinate: Coordinate = Coordinate(0, 0, 0)):
        self.number = number
        self.orthogonal_coordinate = orthogonal_coordinate
        self.new_coordinate_system = new_coordinate_system
        self.new_coordinate = new_coordinate

    def direct_conversion(self):

        pass


if __name__ == '__main__':

    print(Dot(
        number=1,
        orthogonal_coordinate=Coordinate(x=1, y=2, z=3),
        new_coordinate_system=CoordinateSystem(
            ox=Coordinate(3, 5, 2),
            oy=Coordinate(5, 32, 14),
            oz=Coordinate(12, 33, 41))).__dict__)
