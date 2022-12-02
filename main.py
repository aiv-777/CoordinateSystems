import numpy as np


class CoordinateSystem:
    def __init__(self,
                 o: np.array,
                 ox: np.array,
                 oy: np.array,
                 oz: np.array):
        self.o = o  # Начало новой системы координат О
        self.ox = (ox - self.o)/np.linalg.norm(ox - self.o)  # Ось Ox
        self.oy = (oy - self.o)/np.linalg.norm(oy - self.o)  # Ось Oy
        self.oz = (oz - self.o)/np.linalg.norm(oz - self.o)  # Ось Oz


class Dot:
    def __init__(self,
                 x: float,
                 y: float,
                 z: float):
        self.x = x  # Координата x
        self.y = y  # Координата y
        self.z = z  # Координата z

    @staticmethod
    def direct_projection(axis: np.array, vector: np.array):
        """Находит проекцию точки на новую ось"""
        return np.dot(axis, vector)

    def direct_conversion(self, coordinate_system: CoordinateSystem):
        """Преобразование координат из стартовой ортогональной системы
        в новую систему"""
        vector = np.array([self.x - coordinate_system.o[0],
                           self.y - coordinate_system.o[1],
                           self.z - coordinate_system.o[2]])
        self.x = self.direct_projection(coordinate_system.ox, vector)
        self.y = self.direct_projection(coordinate_system.oy, vector)
        self.z = self.direct_projection(coordinate_system.oz, vector)

    @staticmethod
    def right_piece(axis: np.array,
                    o: np.array,
                    coordinates: np.array,
                    i: int):
        """Находит правую часть уравнения в правой части системы"""
        return np.dot(axis, o) + coordinates[i]

    def reverse_conversion(self, coordinate_system: CoordinateSystem):
        """Преобразование координат из новой системы
                в стартовую ортогональную систему"""
        coordinates = np.array([self.x,
                                self.y,
                                self.z])

        left_part = np.array([coordinate_system.ox,
                              coordinate_system.oy,
                              coordinate_system.oz])

        right_part = np.array([self.right_piece(coordinate_system.ox,
                                                coordinate_system.o,
                                                coordinates, 0),
                               self.right_piece(coordinate_system.oy,
                                                coordinate_system.o,
                                                coordinates, 1),
                               self.right_piece(coordinate_system.oz,
                                                coordinate_system.o,
                                                coordinates, 2)])

        solution = np.linalg.solve(left_part, right_part)
        self.x = solution[0]
        self.y = solution[1]
        self.z = solution[2]


if __name__ == '__main__':
    A = Dot(23, 17, 98)
    print("Исходные координаты точки А\n", A.__dict__)
    sc1 = CoordinateSystem(o=np.array([4, 2, 3]),
                           ox=np.array([4, 5, 2]),
                           oy=np.array([7, 12, 31]),
                           oz=np.array([10, 12, 12])
                           )
    print("Новая система координат\n", sc1.__dict__)
    A.direct_conversion(sc1)
    print("Координаты точки А после прямого преобразования\n", A.__dict__)
    A.reverse_conversion(sc1)
    print("Координаты точки А после обратного преобразования\n", A.__dict__)
