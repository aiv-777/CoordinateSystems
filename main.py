import numpy as np


class CoordinateSystem:
    def __init__(self,
                 o: np.array,
                 ox: np.array,
                 oy: np.array,
                 oz: np.array):
        self.o = o
        self.ox = (ox - self.o)/np.linalg.norm(ox - self.o)
        self.oy = (oy - self.o)/np.linalg.norm(oy - self.o)
        self.oz = (oz - self.o)/np.linalg.norm(oz - self.o)


class Dot:
    def __init__(self,
                 x: float,
                 y: float,
                 z: float):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def direct_projection(axis, vector):
        return np.dot(axis, vector)

    def direct_conversion(self, coordinate_system: CoordinateSystem):
        vector = np.array([self.x - coordinate_system.o[0],
                           self.y - coordinate_system.o[1],
                           self.z - coordinate_system.o[2]])
        self.x = self.direct_projection(coordinate_system.ox, vector)
        self.y = self.direct_projection(coordinate_system.oy, vector)
        self.z = self.direct_projection(coordinate_system.oz, vector)

    @staticmethod
    def right_piece(axis, o, coordinates):
        # res1 = axis*coordinates
        # print("\nRes 1 = \n", res1)
        # res2 = res1 + o
        # print("\nRes 2 = \n", res1)
        # result = res2*axis
        # print("gR =", result)
        RES = sum((axis*coordinates + o)*axis)
        # coefficients = np.array([1,
        #                          np.dot(axis, o),
        #                          np.linalg.norm(o)**2 - coordinates[i]**2])
        # solutions = np.roots(coefficients)
        # for t in solutions:
        #     if np.dot():
        #         return
        return RES

    def reverse_conversion(self, coordinate_system: CoordinateSystem):
        coordinates = np.array([self.x,
                                self.y,
                                self.z])
        print("\nCoordinates:\n", coordinates)

        left_part = np.array([coordinate_system.ox,
                              coordinate_system.oy,
                              coordinate_system.oz])
        print("\nLeft part:\n", left_part)

        right_part = np.array([self.right_piece(coordinate_system.ox,
                                                coordinate_system.o,
                                                coordinates),
                               self.right_piece(coordinate_system.oy,
                                                coordinate_system.o,
                                                coordinates),
                               self.right_piece(coordinate_system.oz,
                                                coordinate_system.o,
                                                coordinates)])
        print("\nRight part:\n", right_part)
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
