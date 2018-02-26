# coding=utf-8
import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def plus(self, other):
        new_coordinates = []
        if self.dimension != other.dimension:
            raise ValueError('two dimension must be equals')
        for index in range(self.dimension):
            new_coordinates.append(self.coordinates[index] + other.coordinates[index])
        return Vector(new_coordinates)

    def plus2(self, other):
        new_coordinates = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def minus(self, other):
        new_coordinates = []
        if self.dimension != other.dimension:
            raise ValueError('two dimension must be equals')
        for index in range(self.dimension):
            new_coordinates.append(self.coordinates[index] - other.coordinates[index])
        return Vector(new_coordinates)

    def minus2(self, other):
        new_coordinates = [x - y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def scalar_multiply(self, scalar):
        new_coordinates = []
        for index in range(self.dimension):
            new_coordinates.append(self.coordinates[index] * scalar)
        return Vector(new_coordinates)

    def scalar_multiply2(self, scalar):
        new_coordinates = [scalar * x for x in self.coordinates]
        return Vector(new_coordinates)

    # 计算向量大小
    def magnitude(self):
        square_sum = 0
        new_coordinates = [x * x for x in self.coordinates]
        for i in range(self.dimension):
            square_sum += new_coordinates[i]
        return math.sqrt(square_sum)

    # 标准化
    def normalized(self):
        magnitude = self.magnitude()
        new_coordinates = [x / magnitude for x in self.coordinates]
        return Vector(new_coordinates)

    # 计算向量点积
    def dot_product(self, other):
        dot_product = 0
        if self.dimension != other.dimension:
            raise ValueError('Two dimension must be equals')
        for i in range(self.dimension):
            dot_product += self.coordinates[i] * other.coordinates[i]
        return dot_product

    # 计算向量夹角rad
    def angle_rad(self, other):
        if self.dimension != other.dimension:
            raise ValueError('Two dimension must be equals')
        dot_product = self.dot_product(other)
        self_magnitude = self.magnitude()
        other_magnitude = other.magnitude()
        if self_magnitude == 0 or other_magnitude == 0:
            return 0
        return math.acos(dot_product / (self_magnitude * other_magnitude))

    # 计算向量夹角degree
    def angle_degrees(self, other):
        return math.degrees(self.angle_rad(other))

    # 计算两个向量是否平行
    def parallelism(self, other, tolerance=1e-10):
        if self.dimension != other.dimension:
            raise ValueError('Two dimension must be equals')
        if self.dimension == 1:
            return 'True'
        if self.magnitude() == 0 or other.magnitude() == 0:
            return 'True'
        first_scala = other.coordinates[0] / self.coordinates[0]
        for i in range(self.dimension - 1):
            other_scala = other.coordinates[i + 1] / self.coordinates[i + 1]
            if abs(first_scala - other_scala) > tolerance:
                return 'False'
        return 'True'

    # 计算两个向量是否正交
    def orthogonality(self, other, tolerance=1e-10):
        return abs(self.dot_product(other)) < tolerance
